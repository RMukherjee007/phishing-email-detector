import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from .preprocessing import TextPreprocessor, URLExtractor

class FeatureExtractor:
    """Combines TF-IDF vocabulary with structural phishing heuristics."""
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.url_extractor = URLExtractor()
        self.vectorizer = TfidfVectorizer(max_features=1500, ngram_range=(1, 2))
        self.is_fitted = False

    def _get_structural_features(self, text: str) -> list:
        # Heuristics: URL count and Urgency-based keywords
        text_lower = text.lower()
        has_urgency = 1 if any(w in text_lower for w in ['urgent', 'verify', 'account', 'suspended', 'action']) else 0
        url_count = self.url_extractor.count(text)
        return [url_count, has_urgency]

    def fit(self, texts: list[str]):
        cleaned = [self.preprocessor.clean(t) for t in texts]
        self.vectorizer.fit(cleaned)
        self.is_fitted = True

    def transform(self, texts: list[str]) -> np.ndarray:
        if not self.is_fitted:
            raise ValueError("FeatureExtractor must be fitted before transform.")
        
        cleaned = [self.preprocessor.clean(t) for t in texts]
        tfidf_matrix = self.vectorizer.transform(cleaned).toarray()
        
        # Append structural features to the TF-IDF matrix
        struct_feats = np.array([self._get_structural_features(t) for t in texts])
        return np.hstack([tfidf_matrix, struct_feats])

    def fit_transform(self, texts: list[str]) -> np.ndarray:
        self.fit(texts)
        return self.transform(texts)
