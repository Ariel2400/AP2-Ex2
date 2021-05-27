import json,os
from flask import Flask, render_template, request, render_template_string
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_DIR = os.getcwd() +'/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file_reg = request.files['reg_csv']
        file_reg_name=os.path.join(app.config['UPLOAD_FOLDER'],file_reg.filename)
        file_reg.save(file_reg_name)
        file_irreg = request.files['irreg_csv']
        file_irreg_name=os.path.join(app.config['UPLOAD_FOLDER'],file_irreg.filename)
        file_irreg.save(file_irreg_name)
        #debug
        print(f"Chosen algorithm: {request.form.get('algorithms')}")
        #here's the function that processes the data and returns json_res
        #dict_res=json.loads(json_res)
        #return render_template('check.html', display_data = True, result=dict_res)

    
    return render_template('check.html', display_data=False, result={})

if __name__ == '__main__':
    app.run(debug=True)