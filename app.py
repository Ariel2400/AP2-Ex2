import os
from flask import Flask, render_template, request,redirect,flash
from werkzeug.utils import secure_filename
UPLOAD_DIR = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file_irreg = request.files['reg_csv']
        file_irreg.save(secure_filename(file_irreg.filename))
        file_reg = request.files['irreg_csv']
        file_reg.save(secure_filename(file_reg.filename))
        print(f"Chosen algorithm: {request.form.get('algorithms')}")
        
    
    return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True)