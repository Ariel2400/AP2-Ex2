from flask import Flask, request
from flask_restful import Api, Resource

from algorithms.LinearAlgorithm import LinearAlgorithm
from algorithms.HybridAlgorithm import HybridAlgorithm

open_file_list =[]

app = Flask(__name__)
api = Api(app)


class MY_API(Resource):

    def post(self):
        algo_type = request.json['algo_type']
        correct_csv = request.json['correct_csv']
        false_csv = request.json['false_csv']
        if algo_type == "HybridAlgorithm":
            x = HybridAlgorithm(correct_csv, false_csv)
        else:
            x = LinearAlgorithm(correct_csv, false_csv)
        return x.detect_anomalies()


api.add_resource(MY_API, "/detect")

if __name__ == "__main__":
    app.run(debug=True)
