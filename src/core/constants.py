""" Contains the project constants. """

from src.core.config import Config
from src.database import schema_dict

run_id = Config.get_run_id()
BASE_DATA_NAME = 'raw_data.csv'

TARGET_NAME = schema_dict['targetColumn']
NUM_COLS = schema_dict['numColumnsNames']
CAT_COLS = schema_dict['catColumnsNames']
ALL_COLS = schema_dict['columnNames']
