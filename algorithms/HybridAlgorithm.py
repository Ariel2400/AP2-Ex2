from pathlib import Path
import json
import pandas as pd

CONFIG_PATH = Path('C:/Users/yairi/OneDrive/Desktop/University/AP2/AP2-Ex2/config/algorithms')


class HybridAlgorithm:

    def __init__(self, path: Path):
        self.data = self._parse_csv(path)

    @staticmethod
    def _parse_csv(path: str) -> dict:
        with open(CONFIG_PATH / 'column_titles.json', 'r') as titles_config:
            titles = list(json.load(titles_config).keys())
        df = pd.read_csv(path)
        row_as_df = pd.DataFrame(list(df.columns), list(df.columns))
        df = row_as_df.transpose().append(df)
        df.columns = titles
        d = df.to_dict()
        return d
