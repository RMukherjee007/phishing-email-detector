import numpy as np
from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from core.preprocessing import TextPreprocessor, URLExtractor


@dataclass
class EmailFeatures:
    matrix: np.ndarray
    feature_names: list[str]


class FeatureExtractor:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.url_extractor = URLExtractor()
        self.vectorizer = TfidfVectorizer(
            max_features=1000, ngram_range=(1, 2), min_df=2, max_df=0.8
        )
        self.is_fitted = False

    def fit(self, texts: list[str]):
        cleaned = [self.preprocessor.clean(t) for t in texts]
        self.vectorizer.fit(cleaned)
        self.is_fitted = True

    def transform(self, texts: list[str]) -> EmailFeatures:
        if not self.is_fitted:
            raise ValueError("FeatureExtractor not fitted")

        cleaned = [self.preprocessor.clean(t) for t in texts]
        tfidf = self.vectorizer.transform(cleaned).toarray()

        urls = np.array([[self.url_extractor.count(t)] for t in texts])
        matrix = np.hstack([tfidf, urls])

        feature_names = list(self.vectorizer.get_feature_names_out()) + ["url_count"]
        return EmailFeatures(matrix=matrix, feature_names=feature_names)

    def fit_transform(self, texts: list[str]) -> EmailFeatures:
        self.fit(texts)
        return self.transform(texts)
