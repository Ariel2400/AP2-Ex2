import json, os
from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_DIR = os.getcwd() + '/uploads'
if not os.path.exists(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not (save_file_to_uploads('train_csv') and save_file_to_uploads('test_csv')):
            return render_template('check.html', display_data=False, result={})
        # debug
        print(f"Chosen algorithm: {request.form.get('algorithms')}")
        # here's the function that processes the data and returns json_res
        json_res = test_json()
        dict_res = json.loads(json_res)
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


def test_json():
    x = {"success": "yes", "failure": "no"}
    return json.dumps(x)


if __name__ == '__main__':
    app.run(debug=True)
