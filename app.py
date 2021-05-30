import json
import os

import requests
from flask import Flask, render_template, request
from flask_restful import Api, Resource

from algorithms.HybridAlgorithm import HybridAlgorithm
from algorithms.LinearAlgorithm import LinearAlgorithm

BASE = 'http://127.0.0.1:5000/detect'
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

UPLOAD_DIR = os.getcwd() + '/uploads'
if not os.path.exists(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not (save_file_to_uploads('reg_csv') and save_file_to_uploads('irreg_csv')):
            return render_template('check.html', display_data=False, result={})
        # debug
        reg_path = os.path.join(app.config['UPLOAD_FOLDER'], request.files['reg_csv'].filename)
        irreg_path = os.path.join(app.config['UPLOAD_FOLDER'], request.files['irreg_csv'].filename)
        algo_type = request.form.get('algorithms')
        response = requests.post(BASE, json={'algo_type': algo_type, 'reg_csv': reg_path, 'irreg_csv': irreg_path})
        res_json = response.json()
        dict_res = json.loads(res_json)
        return render_template('check.html', display_data=True, result=dict_res)

    return render_template('check.html', display_data=False, result={})


def save_file_to_uploads(name: str) -> bool:
    try:
        file_from_request = request.files[name]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_from_request.filename)
        file_from_request.save(file_path)
        return True
    except:
        return False


if __name__ == '__main__':
    app.run(debug=True)
