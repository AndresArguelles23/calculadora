from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suma', methods=['POST'])
def suma():
    data = request.get_json()
    try:
        result = data['num1'] + data['num2']
        return jsonify({'result': result})
    except (TypeError, KeyError):
        return jsonify({'result': 'Error: Entrada no válida'}), 400

@app.route('/resta', methods=['POST'])
def resta():
    data = request.get_json()
    try:
        result = data['num1'] - data['num2']
        return jsonify({'result': result})
    except (TypeError, KeyError):
        return jsonify({'result': 'Error: Entrada no válida'}), 400

@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()
    try:
        result = data['num1'] * data['num2']
        return jsonify({'result': result})
    except (TypeError, KeyError):
        return jsonify({'result': 'Error: Entrada no válida'}), 400

@app.route('/division', methods=['POST'])
def division():
    data = request.get_json()
    try:
        if data['num2'] == 0:
            return jsonify({'result': 'Error: División por cero'}), 400
        result = data['num1'] / data['num2']
        return jsonify({'result': result})
    except (TypeError, KeyError):
        return jsonify({'result': 'Error: Entrada no válida'}), 400

if __name__ == '__main__':
    app.run(debug=True)
