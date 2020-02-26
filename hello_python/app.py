from flask import Flask, Response
import os
from db.db import initialize_db
from db.models import Movie

__version__ = '0.1.0'

app = Flask(__name__)
app.config['MONGODB_DB'] = os.environ['MONGODB_DATABASE']
app.config['MONGODB_HOST'] = os.environ['MONGODB_HOSTNAME']
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = os.environ['MONGODB_USERNAME']
app.config['MONGODB_PASSWORD'] = os.environ['MONGODB_PASSWORD']

# app.config["MONGODB_SETTINGS"] = {
#     'host': 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' +
#     os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] +
#     ':27017/' + os.environ['MONGODB_DATABASE']
# }
initialize_db(app)


@app.route('/')
def index():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
