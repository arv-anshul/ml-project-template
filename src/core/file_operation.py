import shutil
from pathlib import Path

import dill

from src.core.logger import LogFileName, Logger


class FileOperation:
    """Class for file operations."""

    def __init__(self, run_id: str, data_path: str, mode: LogFileName) -> None:
        """
        Initialize the FileOperation class.

        Args:
            run_id (str): The run ID.
            data_path (str): The data path.
            mode (str): The mode.

        Returns:
            None.
        """
        self.run_id = run_id
        self.data_path = data_path
        self.logger = Logger(self.run_id, 'FileOperation', mode)

    def save_model(self, model: object, file_name: Path) -> None:
        """
        Save the model file.

        Args:
            model (object): The model to be saved.
            file_name (Path): The file name.

        Returns:
            str: The success message.
        """
        try:
            self.logger.info('Start of Save Models')
            # Create separate directory for each cluster
            path = Path('apps/models') / file_name
            if path.is_dir():  # Remove previously existing models for each cluster
                shutil.rmtree('apps/models')
                path.mkdir(parents=True, exist_ok=True)
            else:
                path.mkdir(parents=True, exist_ok=True)
            with open(path / (file_name.name + '.sav'), 'wb') as f:
                dill.dump(model, f)
            self.logger.info(f'Model File {file_name} saved')
            self.logger.info('End of Save Models')
        except Exception as e:
            self.logger.exception(f'Exception raised while Save Models: {e}')
            raise Exception()

    def load_model(self, file_name: Path) -> object:
        """
        Load the model file.

        Args:
            file_name (Path): The file name.

        Returns:
            object: The loaded model.
        """
        try:
            self.logger.info('Start of Load Model')
            with open(Path('apps/models') / file_name / (file_name.name + '.sav'), 'rb') as f:
                self.logger.info(f'Model File {file_name} loaded')
                self.logger.info('End of Load Model')
                return dill.load(f)
        except Exception as e:
            self.logger.exception(f'Exception raised while Loading Model: {e}')
            raise Exception()

    def correct_model(self, cluster_number: int) -> str:
        """
        Find the best model.

        Args:
            cluster_number (int): The cluster number.

        Returns:
            str: The model file name.
        """
        try:
            self.logger.info('Start of finding correct model')
            self.cluster_number = cluster_number
            self.folder_name = Path('apps/models')
            self.list_of_model_files = []
            self.list_of_files = list(self.folder_name.iterdir())
            for self.file in self.list_of_files:
                try:
                    if self.file.name.index(str(self.cluster_number)) != -1:
                        self.model_name = self.file.name
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger.info('End of finding correct model')
            return self.model_name
        except Exception as e:
            self.logger.info('Exception raised while finding correct model: ' + str(e))
            raise Exception()
