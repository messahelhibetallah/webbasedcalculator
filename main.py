from flask import Flask, jsonify
from Division import Division
from Addition import Addition
from error import DivisionByZero
from multiplication import Multiplication
from Subtraction import Subtraction

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return '''
    <h3>Welcome </h3>
    <p>To use this calculator you have to follow this format in the URL: /operation/a/b</p>
    '''

@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a,b):
    calculator = Addition()
    return jsonify({'status': 200, 'result': calculator.compute(a,b)})

@app.route('/subtract/<int:a>/<int:b>', methods=['GET'])
def subtract(a,b):
    calculator = Subtraction()
    return jsonify({'status': 200, 'result': calculator.compute(a,b)})


@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a,b):
    calculator = Multiplication()
    return jsonify({'status': 200, 'result': calculator.compute(a,b)})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a,b):
    calculator = Division()
    try:
        result = calculator.compute(a,b)
    except DivisionByZero:
        return jsonify({'status': 200, 'result': 'exception, dividing by zero'})
        
    return jsonify({'status': 200, 'result': result})
