import json
import time
import os

CONFIG_PATH = os.getcwd() + '/config'


def parse_csv(path: str) -> dict:
    with open(CONFIG_PATH + '/algorithms/column_titles.json', 'r') as titles_config:
        titles = list(json.load(titles_config).keys())
    index = 0
    d = dict()
    for title in titles:
        d[title] = dict()
    with open(path, 'r') as csv_file:
        lines = csv_file.readlines()
    for line in lines:
        for val, title in zip(line.split(','), titles):
            d[title][index] = val
        index += 1
    return d
