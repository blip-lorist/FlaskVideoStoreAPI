from video_store import db

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
