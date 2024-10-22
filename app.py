# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 200,
        'message': 'Welcome to the Calculator API',
        'operations_available': [
            '/add/number1/number2',
            '/minus/number1/number2',
            '/multiply/number1/number2',
            '/divide/number1/number2'
        ]
    })

@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    return jsonify({
        'status': 200,
        'result': num1 + num2
    })

@app.route('/minus/<float:num1>/<float:num2>')
def minus(num1, num2):
    return jsonify({
        'status': 200,
        'result': num1 - num2
    })

@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1, num2):
    return jsonify({
        'status': 200,
        'result': num1 * num2
    })

@app.route('/divide/<float:num1>/<float:num2>')
def divide(num1, num2):
    if num2 == 0:
        return jsonify({
            'status': 400,
            'error': 'Division by zero is not allowed'
        }), 400
    return jsonify({
        'status': 200,
        'result': num1 / num2
    })

if __name__ == '__main__':
    app.run(debug=True)
