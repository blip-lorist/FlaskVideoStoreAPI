from video_store import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    registered_at = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    postal_code = db.Column(db.String(200))
    phone = db.Column(db.String(200))

    def __repr__(self):
        return '<Customer %r>' % (self.name)
