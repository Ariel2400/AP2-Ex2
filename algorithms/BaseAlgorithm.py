from pathlib import Path
from algorithms.algorithm_utils import *
import pandas as pd
import socket
import json
import time
import os

CONFIG_PATH = os.getcwd() + '/config'


class BaseAlgorithm:

    def __init__(self, path_to_reg_flight: str, path_to_anomaly_flight: str):
        self.path_to_reg_flight = path_to_reg_flight
        self.path_to_anomaly_flight = path_to_anomaly_flight
        self.reg_flight = parse_csv(self.path_to_reg_flight)
        self.anomaly_flight = parse_csv(self.path_to_anomaly_flight)

    def detect_anomalies(self):
        sock = socket.socket()
        with open(CONFIG_PATH + '/anomaly_detection_config.json', 'r') as ip_config:
            ip_port = json.load(ip_config)
            ip, port = ip_port['ip'], int(ip_port['port'])
        sock.connect((ip, port))
        time.sleep(0.1)
        sock.recv(2048)
        sock.send(b'1\n')
        time.sleep(0.1)
        b = sock.recv(2048)
        assert b == b'Please upload your local train CSV file.\n'
        with open(CONFIG_PATH + '/algorithms/column_titles.json', 'r') as titles:
            sock.send(','.join(list(json.load(titles).keys())).encode()+b'\n')
        with open(self.path_to_reg_flight, 'r') as reg_flight:
            for line in reg_flight.readlines():
                sock.send(line.encode())
            sock.send(b'done\n')
        time.sleep(0.5)
        b = sock.recv(2048)
        assert b == b'Upload complete.\nPlease upload your local test CSV file.\n'
        with open(CONFIG_PATH + '/algorithms/column_titles.json', 'r') as titles:
            sock.send(','.join(list(json.load(titles).keys())).encode()+b'\n')
        with open(self.path_to_anomaly_flight, 'r') as anomaly_flight:
            for line in anomaly_flight.readlines():
                sock.send(line.encode())
            sock.send(b'done\n')
        time.sleep(0.1)
        b = sock.recv(2048)
        return sock
