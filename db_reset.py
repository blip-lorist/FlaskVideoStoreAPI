from video_store.models import Customer, Movie, Rental
from video_store import db
import json

# DB Drop
db.drop_all()

# DB Create
db.create_all()

# DB Seed
# Yay StackOverflow
# (http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python)
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('ascii', 'ignore')
    else:
        return input

# Collect all customers
# The 'with' statement ensures that the file is closed
with open('seeds/customers.json') as seed_customers:
    customers = json.load(seed_customers)
    customers = byteify(customers)

# Create a db record for each customer
for customer in customers:
    name = customer['name']
    registered_at = customer['registered_at']
    address = customer['address']
    city = customer['city']
    state = customer['state']
    postal_code = customer['postal_code']
    phone = customer['phone']
    account_credit = customer['account_credit']
    customer_record = Customer(name, registered_at, address, city, state, postal_code, phone, account_credit)
    db.session.add(customer_record)

    db.session.commit()

with open('seeds/movies.json') as seed_movies:
    movies = json.load(seed_movies)
    movies = byteify(movies)

# Create a db record for each customer
for movie in movies:
    title = movie['title']
    overview = movie['overview']
    release_date = movie['release_date']
    inventory = int(movie['inventory'])
    movie_record = Movie(title, overview, release_date, inventory)
    db.session.add(movie_record)
    db.session.commit()

with open('seeds/rentals.json') as seed_rentals:
    rentals = json.load(seed_rentals)
    rentals = byteify(rentals)

# Create a db record for each customer
for rental in rentals:
    movie_id = rental['movie_id']
    customer_id = rental['customer_id']
    returned_date = rental['returned_date']
    due_date = rental['due_date']
    checked_out = rental['checked_out']
    rental_record = Rental(movie_id, customer_id, returned_date, due_date, checked_out)
    db.session.add(rental_record)
    db.session.commit()
