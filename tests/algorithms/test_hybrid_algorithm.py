from pathlib import Path
from algorithms.HybridAlgorithm import HybridAlgorithm
from algorithms.algorithm_utils import *

def test_parse_csv():
    path = "C:/Users/yairi/OneDrive/Desktop/University/AP2/AP2-Ex2/tests/reg_flight.csv"
    d = parse_csv(path)
    assert len(d) == 42
    assert len(d['aileron']) == 2174

tests = {'test_parse_csv': test_parse_csv}

if __name__ == '__main__':
    for name in tests:
        tests[name]()
