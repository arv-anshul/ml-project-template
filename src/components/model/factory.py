import importlib
from pathlib import Path
from typing import Any, TypeAlias

from pydantic import BaseModel

from src.core import io

CVModels: TypeAlias = dict[str, Any]


class CVClassParams(BaseModel):
    estimator: Any
    param_grid: Any
    scoring: str = "accuracy"
    cv: int = 3
    verbose: int = 3


class CVConfig(BaseModel):
    class_: str
    module: str
    class_params: CVClassParams


class ModelConfig(BaseModel):
    model_id: str
    class_: str
    module: str
    class_params: dict[str, Any] = {}
    param_grid: dict[str, Any]


class _Config(BaseModel):
    models_config: list[ModelConfig]
    cv_config: CVConfig


def create_class(class_config: CVConfig | ModelConfig):
    module = importlib.import_module(class_config.module)
    class_ = getattr(module, class_config.class_)
    return class_(**class_config.class_params)


def create_cv_class(cv_config: CVConfig, model_config: ModelConfig):
    model = create_class(model_config)

    cv_config.class_params.estimator = model
    cv_config.class_params.param_grid = model_config.param_grid

    return create_class(cv_config)


def load_models_from_schema(schema_fp: Path) -> CVModels:
    config_data = io.load_yaml(schema_fp)
    config = _Config(**config_data)

    cv_models = {}
    for model_config in config.models_config:
        cv_model = create_cv_class(config.cv_config, model_config)
        cv_models[model_config.model_id] = cv_model

    return cv_models
