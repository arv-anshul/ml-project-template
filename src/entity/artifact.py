""" Entity for artifact folder to store all data and models. """

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, eq=False, slots=True)
class DataIngestionArtifact:
    feature_store_path: Path
    train_path: Path
    test_path: Path


@dataclass(frozen=True, eq=False, slots=True)
class DataValidationArtifact(DataIngestionArtifact):
    report_path: Path


@dataclass(frozen=True, eq=False, slots=True)
class DataTransformationArtifact:
    transformer_pkl: Path
    target_enc_path: Path
    train_npz_path: Path
    test_npz_path: Path


@dataclass(frozen=True, eq=False, slots=True)
class ModelTrainerArtifact:
    model_path: Path
    train_score: float
    test_score: float


@dataclass(frozen=True, eq=False, slots=True)
class ModelEvaluationArtifact:
    is_model_accepted: bool
    improved_accuracy: float


@dataclass(frozen=True, eq=False, slots=True)
class ModelPusherArtifact:
    self_dir: Path
    stored_model_dir: Path
