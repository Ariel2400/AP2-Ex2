from pathlib import Path
import pandas as pd
import json
import os

CONFIG_PATH = os.getcwd() + '/config'

class HybridAlgorithm:

    def __init__(self, path: Path):
        self.data = self._parse_csv(path)

    @staticmethod
    def _parse_csv(path: str) -> dict:
        with open(CONFIG_PATH + '/algorithms/column_titles.json', 'r') as titles_config:
            titles = list(json.load(titles_config).keys())
        df = pd.read_csv(path)
        row_as_df = pd.DataFrame(list(df.columns), list(df.columns))
        df = row_as_df.transpose().append(df)
        df.columns = titles
        d = df.to_dict()
        return d
