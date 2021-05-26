import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE, json={"algo_type": "hybrid",
                                     "correct_csv": {'key1': [1, 2, 3], 'key2': [4, 5, 6]},
                                     "false_csv": 2})
print(response.json())
