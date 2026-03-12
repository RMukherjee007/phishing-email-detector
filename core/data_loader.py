import pandas as pd
from dataclasses import dataclass

@dataclass
class EmailData:
    texts: list[str]
    labels: list[int]

class DataLoader:
    """Handles dataset ingestion and basic validation for training."""
    def load_from_csv(self, path: str, text_col: str = "text", label_col: str = "label") -> EmailData:
        df = pd.read_csv(path)
        
        if text_col not in df.columns or label_col not in df.columns:
            raise ValueError(f"CSV must contain columns: {text_col} and {label_col}")

        df = df.dropna(subset=[text_col, label_col])
        return EmailData(
            texts=df[text_col].astype(str).tolist(),
            labels=df[label_col].astype(int).tolist()
        )
