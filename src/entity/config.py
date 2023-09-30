from dataclasses import dataclass
from datetime import datetime as dt
from pathlib import Path


class PipelineConfig:
    def __init__(self):
        self.root = Path.cwd()
        self.artifact_dir = Path("artifacts", dt.now().strftime("%m%d%y__%H"))
        self.data_schema_path = self.root / "src/database/schema.json"
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.artifact_dir.mkdir(parents=True, exist_ok=True)


class DataIngestionConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / "data_ingestion"
        self.train_path = self.dir / "train.csv"
        self.test_path = self.dir / "test.csv"
        self.test_size = None  # According to project
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.train_path.parent.mkdir(parents=True, exist_ok=True)


class DataValidationConfig(DataIngestionConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / "data_validation"
        self.reports_dir = self.root / "reports"
        self.drift_report_path = self.reports_dir / "drift_report.yaml"
        self.missing_threshold = None  # According to project
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True)


class DataTransformationConfig(DataIngestionConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / "data_transformation"
        self.transformer_pkl_path = self.dir / "transformer.pkl"
        self.target_enc_path = self.dir / "target_encoder.pkl"
        self.train_np_path = self.dir / "transformed_arrays/train.npy"
        self.test_np_path = self.dir / "transformed_arrays/test.npy"
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)
        self.train_np_path.parent.mkdir(parents=True, exist_ok=True)


class ModelTrainerConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / "model_trainer"
        self.model_path = self.dir / "model.pkl"
        self.model_schema_path = self.root / "config/model_schema.yaml"
        self.expected_training_score = None  # According to project
        self.expected_testing_score = None  # According to project
        self.overfitting_threshold = None  # According to project
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)


@dataclass
class ModelEvaluationConfig:
    model_score_diff_threshold = None  # According to project


class ModelPusherConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / "model_pusher"
        self.model_path = self.dir / "model.pkl"
        self.transformer_path = self.dir / "transformer.pkl"
        self.target_enc_path = self.dir / "target_encoder.pkl"
        self.trained_model_dir = self.root / "trained_models"
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)
