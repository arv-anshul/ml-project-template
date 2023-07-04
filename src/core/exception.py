""" Custom Exception for the project. Shows the filename and line number. """

from functools import wraps
from sys import exc_info
from types import TracebackType
from typing import TypeAlias

from src.core.logger import logging

ExcInfo: TypeAlias = tuple[type[BaseException], BaseException, TracebackType]
OptExcInfo: TypeAlias = ExcInfo | tuple[None, None, None]


class CustomException(Exception):
    def __init__(
        self,
        error_message: Exception | str,
        error_detail: OptExcInfo,
    ) -> None:
        super().__init__(error_message)
        self.error_message = CustomException.error_message_detail(
            error_message, error_detail)

    @staticmethod
    def error_message_detail(
        error: Exception | str,
        error_detail: OptExcInfo,
    ) -> str:
        """
        error: Exception object raise from module.
        error_detail: `sys.exc_info()`
        """
        _, _, exc_tb = error_detail
        if exc_tb is not None:
            # Extracting file name from exception traceback
            file_name = exc_tb.tb_frame.f_code.co_filename
            # Preparing error message
            message = f'"{file_name}":[{exc_tb.tb_lineno}] - {error}'
        else:
            message = 'No error details available for the raised exception.'
        logging.error(message)
        return message

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        """ Formatting object of AppException """
        return CustomException.__name__.__str__()

    @classmethod
    def wrap_try_except_block(cls):
        """
        Wraps all methods of a class in a try-except block and raises CustomException.
        """
        def wrapper(method):
            @wraps(method)
            def wrapped(*args, **kwargs):
                try:
                    return method(*args, **kwargs)
                except Exception as e:
                    raise CustomException(e, exc_info()) from e
            return wrapped
        for name, method in vars(cls) . items():
            if callable(method):
                setattr(cls, name, wrapper(method))
        return cls
