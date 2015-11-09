from video_store import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    registered_at = db.Column(db.String(200))
    address = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    postal_code = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    account_credit = db.Column(db.String(200))

    def __init__(self, id, name, registered_at, address, city, state, postal_code, phone, account_credit):
        self.id = id
        self.name = name
        self.registered_at = registered_at
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone = phone
        self.account_credit = account_credit

    def __repr__(self):
        return '<Customer %r>' % (self.name)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    overview = db.Column(db.String(200))
    release_date = db.Column(db.String(200))
    inventory = db.Column(db.Integer)

    def __init__(self, title, overview, release_date, inventory):
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.inventory = inventory

    def __repr__(self):
        return '<Movie %r>' % (self.name)
