from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

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
    #df.to_excel('excel_output.xlsx', index=False)
    return 'Excel file created!'

if __name__ == '__main__':
    app.run()
