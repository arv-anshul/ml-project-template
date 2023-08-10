from dataclasses import dataclass

import yaml

schema_dict: dict = yaml.safe_load(open('src/database/schema.yaml'))


@dataclass(init=False)
class DataSchema:
    number_of_cols: int = schema_dict['number_of_columns']
    target_name: str = schema_dict['target_column']
    all_cols: list[str] = schema_dict['columns']
    num_cols: list[str] = schema_dict['num_columns']
    cat_cols: list[str] = schema_dict['cat_columns']
