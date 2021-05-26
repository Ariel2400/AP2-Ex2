from pathlib import Path
from algorithms.algorithm_utils import *
import pandas as pd
import socket
import json
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
        with open(CONFIG_PATH / '/anomaly_detection_config.json', 'r') as ip_config:
            ip_port = json.load(ip_config)
            ip, port = ip_port['ip'], int(ip_port['port'])
        sock.connect((ip, port))
        sock.recv(2048)
        sock.send(b'1\n')
        sock.recv(2048)
        for i in range(len(self.reg_flight['aileron'])):
            line = ''
            for key in self.reg_flight:
                line += self.reg_flight[key][i] + ','
            line = line[0:len(line)-1]
            sock.send(line.encode+b'\n')
        sock.send(b'done\n')
        for i in range(len(self.anomaly_flight['aileron'])):
            line = ''
            for key in self.anomaly_flight:
                line += self.anomaly_flight[key][i] + ','
            line = line[0:len(line)-1]
            sock.send(line.encode+b'\n')
        sock.send(b'done\n')
        return sock
        
            


