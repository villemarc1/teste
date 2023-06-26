from flask import Flask, jsonify, request, render_template
import pandas as pd
import os

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


if __name__ == '__main__':
    app.run()
