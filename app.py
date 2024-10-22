from flask import Flask, jsonify, render_template# type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add/<float:a>/<float:b>', methods=['GET'])
def add(a, b):
    result = a + b
    return jsonify({'status': 200, 'result': result})

@app.route('/subtract/<float:a>/<float:b>', methods=['GET'])
def subtract(a, b):
    result = a - b
    return jsonify({'status': 200, 'result': result})

@app.route('/multiply/<float:a>/<float:b>', methods=['GET'])
def multiply(a, b):
    result = a * b
    return jsonify({'status': 200, 'result': result})

@app.route('/divide/<float:a>/<float:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return jsonify({'status': 400, 'error': 'Division by zero is not allowed'}), 400
    result = a / b
    return jsonify({'status': 200, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
