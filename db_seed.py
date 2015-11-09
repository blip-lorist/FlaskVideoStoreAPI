from video_store.models import Customer
from video_store import db
import json

# Yay StackOverflow
# (http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python)
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('ascii')
    else:
        return input

# Collect all customers
# The 'with' statement ensures that the file is closed
with open('customers.json') as seed_customers:
    customers = json.load(seed_customers)
    customers = byteify(customers)

# Create a db record for each customer
for customer in customers:
    id = int(customer['id'])
    name = customer['name']
    registered_at = customer['registered_at']
    address = customer['address']
    city = customer['city']
    state = customer['state']
    postal_code = customer['postal_code']
    phone = customer['phone']
    account_credit = customer['account_credit']
    customer_record = Customer(id, name, registered_at, address, city, state, postal_code, phone, account_credit)
    db.session.add(customer_record)
    db.session.commit()
