from algorithms.algorithm_utils import *
from algorithms.BaseAlgorithm import BaseAlgorithm
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
        d = dict()
        for line in b.split('\n'):
            if line == 'Done.':
                break
            time_stamp, desc = line.split('\t')[0], line[line.index('\t') + 1:]
            d[time_stamp] = desc
        return json.dumps(d)


