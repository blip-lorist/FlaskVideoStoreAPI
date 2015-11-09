from video_store import app

@app.route('/')
@app.route('/index')
def index():
    return "Video Store API!"

# ____ CUSTOMER ENDPOINTS ____

# GET all customers
# /customers
@app.route('/customers/')
def customers():
    return "List of customers!"

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
