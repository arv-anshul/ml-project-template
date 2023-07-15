import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypeAlias

from src.core import run_mode
from src.core.constants import run_id


def get_logger(logger_name: str) -> logging.Logger:
    """
    :logger_name (str): `__name__`

    :returns: Logger
    """
    return Logger(logger_name).get_logger


@dataclass
class Logger:
    """
    Logger for the project.

    Args:
        logger_name: __name__
        mode: Literal['training', 'prediction']
    """

    logger_name: str

    def __post_init__(self):
        self.logger = logging.getLogger(self.logger_name)
        self.run_id = run_id
        self.logger.setLevel(logging.DEBUG)

        fp = Path(
            f'logs/{run_mode}_logs/{self.run_id}.log'
        )
        fp.parent.mkdir(parents=True, exist_ok=True)

        formatter = logging.Formatter(
            "[ %(asctime)s ] %(filename)s:[%(lineno)d] - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(fp)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    @property
    def get_logger(self) -> logging.Logger:
        """ Get the Logger object. """
        return self.logger
