from algorithms.algorithm_utils import *
from algorithms.BaseAlgorithm import BaseAlgorithm, parse_lines_to_dict
import json
import os

CONFIG_PATH = os.getcwd() + '/config'


class LinearAlgorithm(BaseAlgorithm):

    def __init__(self, path_to_reg_flight: str, path_to_anomaly_flight: str):
        super().__init__(path_to_reg_flight, path_to_anomaly_flight)

    def detect_anomalies(self):
        sock = super().detect_anomalies()
        sock.send(b'4\n')  # anomaly detection with hybrid algorithm
        time.sleep(0.5)
        b = sock.recv(2048)
        time.sleep(0.1)
        sock.send(b'5\n')
        time.sleep(0.1)
        sock.recv(9)
        time.sleep(0.5)
        b = sock.recv(100000000).decode()
        lines = b.split('\n')
        d = parse_lines_to_dict(lines)
        return json.dumps(d)
