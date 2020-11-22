#from flask import Blueprint,Response,request
from flask import Response,request
from database.models import Movie
from flask_restful import Resource

#movies=Blueprint('movies',_name_)

class MoviesApi(Resource):
  def get(self):
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)
  
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
    movie = Movie.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)














#@app.route('/movies')
#@movies.route('/movies')
#def get_movies():
 #movies = Movie.objects().to_json()
 #return Response(movies, mimetype="application/json", status=200)

#@app.route('/movies', methods=['POST'])
#@movies.route('/movies', methods=['POST'])
#def add_movie():
 #body = request.get_json()
 #movie = Movie(**body).save()
 #id = movie.id
 #return {'id': str(id)}, 200

#@app.route('/movies/<id>', methods=['PUT'])
#@movies.route('/movies/<id>', methods=['PUT'])
#def update_movie(id):
 #body = request.get_json()
 #Movie.objects.get(id=id).update(**body)
 #return '', 200

#@app.route('/movies/<id>', methods=['DELETE'])
#@movies.route('/movies/<id>', methods=['DELETE'])
##movie = Movie.objects.get(id=id).delete()
 #return '', 200

#@app.route('/movies/<id>')
#@movies.route('/movies/<id>')
#def get_movie(id):
 #movies = Movie.objects.get(id=id).to_json()
 #return Response(movies, mimetype="application/json", status=200)