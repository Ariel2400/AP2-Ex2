from pathlib import Path
from algorithms.algorithm_utils import *
from algorithms.BaseAlgorithm import BaseAlgorithm
import pandas as pd
import socket
import json
import os

CONFIG_PATH = os.getcwd() + '/config'


class HybridAlgorithm(BaseAlgorithm):

    def __init__(self, path: str):
        super().__init__(path)

    def detect_anomalies(self):
        sock = super().detect_anomalies()
        sock.send(b'3\n') # anomaly detection with hybrid algorithm
        sock.send(b'5\n')
        b = sock.recv(100000).decode() # get anomaly detection results
        d = dict()
        for line in b.split('\n'):
            time, desc = line.split('\t')[0], line.split('\t')[1]
            d[time] = desc
        return json.dumps(d)



