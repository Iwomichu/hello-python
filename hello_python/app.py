from flask import Flask, Response, request
import os
from db.db import initialize_db
from db.models import Movies

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


@app.route('/movies')
def get_movies():
    movies = Movies.objects().to_json()
    return Response(movies, mimetype='application/json', status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movies(**body).save()
    id = movie.id
    return {'id': str(id)}, 200


@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movies.objects.get(id=id).update(**body)
    return '', 200


@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movies.objects.get(id=id).delete()
    return '', 200


@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    movie = Movies.objects.get(id=id).to_json()
    return Response(movie, mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
