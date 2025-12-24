import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class TextPreprocessor:
    def __init__(self):
        self._ensure_nltk()
        self.stopwords = set(stopwords.words("english"))

    def _ensure_nltk(self):
        for pkg in ["punkt", "stopwords"]:
            try:
                nltk.data.find(pkg)
            except LookupError:
                nltk.download(pkg, quiet=True)

    def clean(self, text: str) -> str:
        if not text:
            return ""
        text = text.lower()
        text = re.sub(r"http\S+", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def tokenize(self, text: str) -> list[str]:
        tokens = word_tokenize(self.clean(text))
        return [t for t in tokens if t.isalpha() and t not in self.stopwords]


class URLExtractor:
    PATTERN = re.compile(r"http[s]?://\S+")

    def count(self, text: str) -> int:
        return len(self.PATTERN.findall(text or ""))
