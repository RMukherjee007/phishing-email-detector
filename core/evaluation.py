from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from dataclasses import dataclass

@dataclass
class EvaluationMetrics:
    accuracy: float
    precision: float
    recall: float
    f1: float

class ModelEvaluator:
    """Computes standard classification metrics for model validation."""
    def evaluate(self, y_true: list[int], y_pred: list[int]) -> EvaluationMetrics:
        return EvaluationMetrics(
            accuracy=accuracy_score(y_true, y_pred),
            precision=precision_score(y_true, y_pred, zero_division=0),
            recall=recall_score(y_true, y_pred, zero_division=0),
            f1=f1_score(y_true, y_pred, zero_division=0)
        )
