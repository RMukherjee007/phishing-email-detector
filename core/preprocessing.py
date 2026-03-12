import re
import nltk
from nltk.corpus import stopwords

class TextPreprocessor:
    """Handles NLTK dependencies and text sanitization."""
    def __init__(self):
        self._ensure_nltk()
        self.stop_words = set(stopwords.words("english"))

    def _ensure_nltk(self):
        # Fix: Precise path checking to prevent redundant downloads or crashes
        for pkg in ["punkt", "stopwords"]:
            try:
                nltk.data.find(f"tokenizers/{pkg}" if pkg == "punkt" else f"corpora/{pkg}")
            except LookupError:
                nltk.download(pkg, quiet=True)

    def clean(self, text: str) -> str:
        if not text: return ""
        text = text.lower()
        # Remove URLs for TF-IDF but keep for the separate URL extractor
        text = re.sub(r"http\S+|www\S+", " ", text)
        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

class URLExtractor:
    """Detects standard and common obfuscated URL patterns."""
    PATTERN = re.compile(r"(http[s]?://\S+|www\.\S+|\S+\.\w{2,4}/\S*)")

    def count(self, text: str) -> int:
        return len(self.PATTERN.findall(text or ""))
