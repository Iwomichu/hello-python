from flask import Response, request
from flask_restful import Resource
from db.models import Movie


class MoviesApi(Resource):
    def get(self):
        data = Movie.objects().to_json()
        return Response(data, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200


class MovieApi(Resource):
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Movie.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        movie = Movie.objects.get(id=id).to_json()
        return Response(movie, mimetype='application/json', status=200)
