import flask
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class MY_API(Resource):

    def post(self):
        algo_type = request.json['algo_type']
        correct_csv = request.json['correct_csv']
        false_csv = request.json['false_csv']
        print(algo_type)
        print(correct_csv)
        print(false_csv)
        return {"status": 202}


api.add_resource(MY_API, "/")

if __name__ == "__main__":
    app.run(debug=True)
