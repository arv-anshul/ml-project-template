from dataclasses import dataclass
from datetime import datetime

from sklearn.ensemble import RandomForestClassifier


@dataclass(init=False)
class Config:
    """ Class for configuration instance attributes. """

    def get_run_id(self) -> str:
        """
        Get the unique run ID.

        Returns:
            str: The unique run ID.
        """
        now = datetime.now()
        date = now.date()
        current_time = now.strftime("%H%M%S")
        return f"{date}_{current_time}"
