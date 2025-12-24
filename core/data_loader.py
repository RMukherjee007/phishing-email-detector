import pandas as pd
from dataclasses import dataclass


@dataclass
class EmailData:
    texts: list[str]
    labels: list[int]

    def validate(self):
        if not self.texts:
            raise ValueError("Dataset is empty")
        if len(self.texts) != len(self.labels):
            raise ValueError("Texts and labels must have same length")


class DataLoader:
    def __init__(self, text_column: str = "text", label_column: str = "label"):
        self.text_column = text_column
        self.label_column = label_column

    def load_from_csv(self, path: str) -> EmailData:
        df = pd.read_csv(path)

        if self.text_column not in df.columns or self.label_column not in df.columns:
            raise ValueError("CSV must contain text and label columns")

        df = df.dropna(subset=[self.text_column, self.label_column])
        data = EmailData(
            texts=df[self.text_column].astype(str).tolist(),
            labels=df[self.label_column].astype(int).tolist(),
        )
        data.validate()
        return data
