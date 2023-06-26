from flask import Flask, jsonify, request, render_template
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'    #nova lina
stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

@app.route('/')
def home():
    return '<h1> teste do 2 deploy </h1>'

@app.route('/create_excel')
def create_excel():
    data = {'Column 1': ['Data 1']}
    df = pd.DataFrame(data)
    df.to_excel('excel_output.xlsx', index=False)
    return 'Excel file created!'

@app.route('/read_excel')
def read_excel():
    filename = 'excel_output.xlsx'  # Nome do arquivo a ser exibido
    #filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_excel(filename)
    return df.to_html()

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    filename = secure_filename(file.filename)
    #filename = file.filename
    file.save(filename)

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
