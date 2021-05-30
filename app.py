import json
import os

import requests
from flask import Flask, render_template, request
from flask_restful import Api, Resource

from algorithms.HybridAlgorithm import HybridAlgorithm
from algorithms.LinearAlgorithm import LinearAlgorithm

BASE = 'http://127.0.0.1:8080/detect'
app = Flask(__name__)
api = Api(app)


# the post request to detect anomalies:
class MY_API(Resource):

    def post(self) -> str:
        algo_type = request.json['algo_type']
        correct_csv = request.json['reg_csv']
        false_csv = request.json['irreg_csv']
        if algo_type == "hybrid":
            x = HybridAlgorithm(correct_csv, false_csv)
        else:
            x = LinearAlgorithm(correct_csv, false_csv)
        x_detect = x.detect_anomalies()
        return x_detect


api.add_resource(MY_API, "/detect")

# set upload directory
UPLOAD_DIR = os.getcwd() + '/uploads'
if not os.path.exists(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR


@app.route('/', methods=["GET", "POST"])
def index():
    # when user hits 'submit', they send a post request
    if request.method == "POST":
        # check if files have been saved
        if not (save_file_to_uploads('reg_csv') and save_file_to_uploads('irreg_csv')):
            return render_template('check.html', display_data=False, result={})
        reg_path = get_path_in_uploads('reg_csv')
        irreg_path = get_path_in_uploads('irreg_csv')
        algo_type = request.form.get('algorithms')
        # send a POST request to the API
        response = requests.post(BASE, json={'algo_type': algo_type, 'reg_csv': reg_path, 'irreg_csv': irreg_path})
        res_json = response.json()
        # parse the json into dict
        dict_res = json.loads(res_json)
        anom_list = dict_res['anomalies']
        return render_template('check.html', display_data=True, result=anom_list)
    # if no request has been made, return the regular form
    return render_template('check.html', display_data=False, result={})


"""
a function that returns the path of the file
:arg attr_name: the type of the file(should be reg_csv/irreg_csv)

:returns: the path of the file in the uploads dir
"""


def get_path_in_uploads(attr_name: str) -> str:
    return os.path.join(app.config['UPLOAD_FOLDER'], request.files[attr_name].filename)


"""
saves the file from the form to uploads dir

:returns: True if save was successful, False otherwise
"""


def save_file_to_uploads(name: str) -> bool:
    try:
        file_from_request = request.files[name]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_from_request.filename)
        file_from_request.save(file_path)
        return True
    except:
        return False


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
