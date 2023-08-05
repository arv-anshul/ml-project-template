from pathlib import Path
from typing import Any

import dill
import numpy as np

from src.core.logger import get_logger

logger = get_logger(__name__)


def dump_model(model: Any, fp: Path) -> None:
    with open(fp, 'wb') as f:
        dill.dump(model, f)
    logger.info('Model dumped at "%s"', fp)


def load_model(fp: Path) -> Any:
    with open(fp, 'rb') as f:
        logger.info('Model loading from "%s"', fp)
        return dill.load(f)


def dump_array(array: np.ndarray, fp: Path) -> None:
    array.dump(fp)
    logger.info('Array dumped at "%s"', fp)


def load_array(fp: Path) -> np.ndarray:
    logger.info('Array loading from "%s"', fp)
    return np.load(fp)
