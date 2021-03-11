from app import db

class Vegetables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    colour = db.Column(db.String(120), index=True)
    flavour = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Vegetables {}>'.format(self.name)

