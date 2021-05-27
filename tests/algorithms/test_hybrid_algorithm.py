from algorithms.algorithm_utils import *
from algorithms.HybridAlgorithm import HybridAlgorithm
import os


def test_detect_anomalies():
    first_path = os.getcwd() + "/tests/reg_flight.csv"
    second_path = os.getcwd() + "/tests/anomaly_flight.csv"
    jsn = HybridAlgorithm(first_path, second_path).detect_anomalies()
    print(json.loads(jsn))