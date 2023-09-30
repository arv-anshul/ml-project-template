class ModelFactoryException(Exception):
    """Base exception class for `model.factory` module."""


class InvalidMLModel(ModelFactoryException):
    """Raises when error occurred while importing ML model in `model.factory`."""


class InvalidCVModel(ModelFactoryException):
    """Raises when error occurred while importing CV class in `model.factory`."""
