import logging
from pathlib import Path
from typing import Literal, TypeAlias

LogLevel: TypeAlias = Literal['debug', 'info', 'warn', 'error', 'critical']
LogFileName: TypeAlias = Literal['training', 'prediction']


class Logger:
    def __init__(
        self, run_id: str, log_module: str,
        log_file_name: LogFileName,
    ) -> None:
        """Logger for the project."""

        self.logger = logging.getLogger(f'{log_module}_{run_id}')
        self.logger.setLevel(logging.DEBUG)

        if log_file_name == 'training':
            file_path: Path = Path(
                f'logs/training_logs/train_log_{run_id}.log'
            )
        else:
            file_path: Path = Path(
                f'logs/prediction_logs/predict_log_{run_id}.log'
            )

        formatter: logging.Formatter = logging.Formatter(
            "[ %(asctime)s ] %(filename)s:[%(lineno)d] - %(levelname)s - %(message)s"
        )

        file_handler: logging.FileHandler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message: str) -> None:
        """Log an info-level message."""
        self.logger.info(message)

    def exception(self, message: str) -> None:
        """Log an exception-level message."""
        self.logger.exception(message)

    def log(self, log_level: LogLevel, message: str) -> None:
        """Log a message with the specified log level."""
        getattr(self.logger, log_level)(message)
