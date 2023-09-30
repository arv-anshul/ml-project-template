from importlib import import_module
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError
from rich import print

from src.core import io
from src.core.errors import InvalidCVModel, InvalidMLModel, ModelFactoryException


class ClassConstructorConfig(BaseModel):
    class_: str
    module: str
    params: dict[str, Any] = {}


class MLModelConfig(BaseModel):
    modelId: str
    classConstructorConfig: ClassConstructorConfig
    paramGrid: dict[str, Any] = {}


class ModelSchema(BaseModel):
    cvConfig: ClassConstructorConfig
    mlModelsConfig: list[MLModelConfig]


def _create_class(constructor_config: ClassConstructorConfig) -> Any:
    """
    Create an instance of a class based on its configuration.

    Args:
        constructor_config (ClassConstructorConfig): Configuration for the class.

    Returns:
        Any: An instance of the class.
    """
    module = import_module(constructor_config.module)
    class_ = getattr(module, constructor_config.class_)
    return class_(**constructor_config.params)


def _create_cv_instance(
    *,
    cv_config: ClassConstructorConfig,
    ml_instance: Any,
    param_grid: dict,
) -> Any:
    """
    Create a cross-validation class from specified parameters.

    Args:
        cv_config (ClassConstructorConfig): Configuration for the cross-validation class.
        ml_instance (Any): The machine learning model instance.
        param_grid (dict): Parameter grid for hyperparameter tuning.

    Returns:
        Any: An instance of the cross-validation class.
    """
    cv_config.params["estimator"] = ml_instance
    cv_config.params["param_grid"] = param_grid

    try:
        cv_instance = _create_class(cv_config)
    except (AttributeError, ModuleNotFoundError) as e:
        raise InvalidCVModel(e)

    return cv_instance


def load_models_from_schema(
    model_schema_path: Path,
    *,
    wrap_with_cv_class: bool = True,
) -> dict[str, Any]:
    """
    Load machine learning and cross-validation models from a YAML configuration file.

    Args:
        model_schema_path (Path): The file path to the YAML configuration file.
        wrap_with_cv_class (bool): You can specify whether you want to wrap with
        cross-validator class. Defaults to True.

    Returns:
        dict[str, Any]: A dictionary mapping model IDs to their corresponding instances
        wrapped with cross-validation class (if specified).
    """
    schema_data = io.load_yaml(model_schema_path)
    try:
        model_schema = ModelSchema(**schema_data)
    except ValidationError as e:
        print(
            "[red]There is some validation error while validating "
            f"'{model_schema_path}'.[/red]"
        )
        raise ModelFactoryException(e)

    models = {}
    for model_config in model_schema.mlModelsConfig:
        try:
            ml_instance = _create_class(model_config.classConstructorConfig)
        except (AttributeError, ModuleNotFoundError) as e:
            raise InvalidMLModel(e)

        if wrap_with_cv_class:
            models[model_config.modelId] = _create_cv_instance(
                cv_config=model_schema.cvConfig,
                ml_instance=ml_instance,
                param_grid=model_config.paramGrid,
            )
        else:
            models[model_config.modelId] = ml_instance

    return models
