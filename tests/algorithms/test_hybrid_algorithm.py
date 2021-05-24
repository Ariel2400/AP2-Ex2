from pathlib import Path
from algorithms.HybridAlgorithm import HybridAlgorithm


def test_parse_csv():
    path = "C:/Users/yairi/OneDrive/Desktop/University/AP2/AP2-Ex2/tests/reg_flight.csv"
    d = HybridAlgorithm._parse_csv(path)
    print(d.keys())
    print(len(d.keys()))
    print(d['latitude-deg'])

tests = {'test_parse_csv': test_parse_csv}

if __name__ == '__main__':
    for name in tests:
        tests[name]()
