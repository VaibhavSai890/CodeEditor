from flask import Flask, request, render_template, jsonify
from runner import run_python_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    inputs = request.json.get('inputs', [])
    output = run_python_code(code, inputs)
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
