from db import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(32), nullable=False)
    location = db.Column(db.String(120))
    description = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
