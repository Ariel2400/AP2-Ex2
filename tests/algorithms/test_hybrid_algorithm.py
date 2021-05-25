from algorithms.algorithm_utils import *
import os


def test_parse_csv():
    path = f"{os.getcwd()}/tests/reg_flight.csv"
    d = parse_csv(path)
    assert len(d) == 42
    assert len(d['aileron']) == 2174


tests = {'test_parse_csv': test_parse_csv}

if __name__ == '__main__':
    for name in tests:
        tests[name]()
