from algorithms.algorithm_utils import *
from algorithms.BaseAlgorithm import BaseAlgorithm
import json
import os

CONFIG_PATH = os.getcwd() + '/config'


class HybridAlgorithm(BaseAlgorithm):

    def __init__(self, path_to_reg_flight: str, path_to_anomaly_flight: str):
        super().__init__(path_to_reg_flight, path_to_anomaly_flight)

    def detect_anomalies(self):
        sock = super().detect_anomalies()
        sock.send(b'4\n') # anomaly detection with linear regression
        sock.send(b'5\n')
        b = sock.recv(100000).decode() # get anomaly detection results
        d = dict()
        for line in b.split('\n'):
            time, desc = line.split('\t')[0], line.split('\t')[1]
            d[time] = desc
        return json.dumps(d)


