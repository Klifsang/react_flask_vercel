from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS = CORS(app)

@app.route('/hello')
def hello_world():
    return jsonify({'title': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
