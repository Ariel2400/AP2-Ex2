import pandas as pd
import json
import os

CONFIG_PATH = os.getcwd() + '/config'


def parse_csv(path: str) -> dict:
    with open(CONFIG_PATH + '/algorithms/column_titles.json', 'r') as titles_config:
        titles = list(json.load(titles_config).keys())
    df = pd.read_csv(path)
    row_as_df = pd.DataFrame(list(df.columns), list(df.columns))
    df = row_as_df.transpose().append(df, ignore_index=True)
    df.columns = titles
    d = df.to_dict()
    return d


def start_server():
    path_to_AP1_Code = os.getcwd() + '/AP1_Code'
    if 'a.out' not in os.listdir(path_to_AP1_Code):
        oldpwd = os.getcwd()
        os.chdir(path_to_AP1_Code)
        os.system('make')
        os.chdir(oldpwd)
    with open(CONFIG_PATH + '/anomaly_detection_config.json', 'r') as ip_config:
        d = json.load(ip_config)
        os.system(f'{path_to_AP1_Code}/a.out {int(d["port"])} &')
        print('hello')
