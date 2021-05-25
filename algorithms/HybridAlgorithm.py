from pathlib import Path
from algorithms.algorithm_utils import *
import pandas as pd
import json
# import pyod
import os

CONFIG_PATH = os.getcwd() + '/config'


class HybridAlgorithm:

    def __init__(self, path: str):
        self.data = parse_csv(path)
