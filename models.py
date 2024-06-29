from flask_sqlalchemy import SQLAlchemy

IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"
# Image taken from solution

db = SQLAlchemy()

class Pet(db.Model):
    """This models a pet potentially available for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, server_default=IMAGE)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    


def connect_db(app):
    """Connects to Flask app"""
    db.app = app
    db.init_app(app)