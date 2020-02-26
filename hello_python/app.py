from flask import Flask

__version__ = '0.1.0'

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Dorld!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
