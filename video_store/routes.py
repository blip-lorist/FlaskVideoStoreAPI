from video_store import app, db
from flask import jsonify
from .models import Customer

def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object.
    """
    json = {}
    json['fields'] = {}
    json['pk'] = getattr(model, 'id')

    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json['fields'][col.name] = getattr(model, col.name)

    return dumps([json])

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
    customers = str(Customer.query.all())
    import pdb; pdb.set_trace()
    return jsonify(customers=customers)

# GET subset of customers sorted by name, registered_at, or postal_code
# /customers/name/page1
@app.route('/customers/<column>/page<int:page>')
def customers_subset(column, page):
    return "Subset of customers on page {}!".format(page)


# ____ MOVIES ENDPOINTS ____

# GET all movies
# /movies
@app.route('/movies/')
def movies():
    return "List of movies!"

# GET subset of movies sorted by title or release_date
# /movies/name/page1
@app.route('/movies/<column>/page<int:page>')
def movies_subset(column, page):
    return "Subset of movies on page {}!".format(page)

# ____ RENTALS ENDPOINTS ____

# GET rental info on a specific movie
@app.route('/rentals/<movie_title>')
def rental_movie(movie_title):
    return "List of rental movies!"
