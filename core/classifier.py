from dataclasses import dataclass
from sklearn.linear_model import LogisticRegression
from .feature_extraction import FeatureExtractor

@dataclass
class PredictionResult:
    label: int
    confidence: float
    label_name: str

class EmailClassifier:
    LABELS = {0: "Legitimate", 1: "Phishing"}

    def __init__(self):
        self.extractor = FeatureExtractor()
        self.model = LogisticRegression(max_iter=1000, class_weight="balanced")
        self.is_trained = False

    def train(self, texts: list[str], labels: list[int]):
        features = self.extractor.fit_transform(texts)
        self.model.fit(features, labels)
        self.is_trained = True

    def predict(self, text: str) -> PredictionResult:
        features = self.extractor.transform([text])
        probs = self.model.predict_proba(features)[0]
        label = probs.argmax()
        return PredictionResult(
            label=int(label),
            confidence=float(probs[label]),
            label_name=self.LABELS[label],
        )
