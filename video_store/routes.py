from video_store import app, db
from flask import jsonify
from .models import Customer, CustomerSchema, Movie, MovieSchema
from sqlalchemy.sql import exists

customers_schema = CustomerSchema(many=True)
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@app.route('/')
@app.route('/index')
def index():
    return "Video Store API!"

@app.route('/zomg')
def it_works():
    return jsonify(zomg="It works!")
# ____ CUSTOMER ENDPOINTS ____

# GET all customers
# /customers
@app.route('/customers/')
def customers():
    customers = Customer.query.all()
    result = customers_schema.dump(customers)
    return jsonify(customers=result.data)

# GET subset of customers sorted by name, registered_at, or postal_code
# /customers/name/page1
@app.route('/customers/<column>/page<int:page>')
def customers_subset(column, page):
    if page <= 1:
        offset = 0
    else:
        offset = (page * 50) - 50

    customers = Customer.query.order_by(column).limit(50).offset(offset)
    result = customers_schema.dump(customers)
    return jsonify(customers=result.data)

# ____ MOVIES ENDPOINTS ____

# GET all movies
# /movies
@app.route('/movies/')
def movies():
    movies = Movie.query.all()
    result = movies_schema.dump(movies)
    return jsonify(movies=result.data)

# GET subset of movies sorted by title or release_date
# /movies/name/page1
@app.route('/movies/<column>/page<int:page>')
def movies_subset(column, page):
    if page <= 1:
        offset = 0
    else:
        offset = (page * 50) - 50

    movies = Movie.query.order_by(column).limit(50).offset(offset)
    result = movies_schema.dump(movies)
    return jsonify(movies=result.data)

# ____ RENTALS ENDPOINTS ____

# GET rental info on a specific movie
@app.route('/rentals/<movie_title>/')
def rental_movie(movie_title):
    movie_title = movie_title.title()
    movie_title = movie_title.encode('ascii', 'ignore')
    movie = Movie.query.filter_by(title=movie_title).first()
    result = movie_schema.dump(movie)
    return jsonify(movies=result.data)
