from pathlib import Path
from algorithms.algorithm_utils import *
import pandas as pd
import socket
import json
import os

CONFIG_PATH = os.getcwd() + '/config'


class HybridAlgorithm:

    def __init__(self, path: str):
        self.sock = socket.socket()

    def train_model(self):
        with open(CONFIG_PATH + '/anomaly_detection_config.json', 'r') as ip_config:
            d = json.load(ip_config)
            self.sock.connect((d['ip'], int(d['port'])))
        self.sock.recv(2048)
        # todo train model

