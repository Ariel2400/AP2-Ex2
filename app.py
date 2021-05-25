import os
from flask import Flask, render_template, request,redirect,flash
from werkzeug.utils import secure_filename
UPLOAD_DIR = "uploads"
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

@app.route('/', methods=["GET", "POST"])
def index():
    # target = os.path.join(app.root_path, "uploads")
    # if not os.path.isdir(target):
    #     os.makedirs(target)
    if request.method == "POST":
    #     f=request.files['reg_csv']
    #     f_name=f.filename
    #     dest='/'.join([target,f_name])
    #     f.save(dest)
        # print('check')


        #in order to det the algorithm name
        print(f"Chosen algorithm: {request.form.get('algorithms')}")
        
    
    return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True)