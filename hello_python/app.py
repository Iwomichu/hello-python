from flask import Flask, jsonify

from db.db import read_bestsellers

__version__ = '0.1.0'

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(read_bestsellers())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
