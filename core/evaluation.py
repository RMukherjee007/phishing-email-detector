from dataclasses import dataclass
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


@dataclass
class EvaluationMetrics:
    accuracy: float
    precision: float
    recall: float
    f1: float


class ModelEvaluator:
    def evaluate(self, true, pred):
        return EvaluationMetrics(
            accuracy_score(true, pred),
            precision_score(true, pred),
            recall_score(true, pred),
            f1_score(true, pred),
        )
