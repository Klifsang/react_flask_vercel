from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS = CORS(app)

@app.route('/')

def hello_world():
    return {'title':'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)