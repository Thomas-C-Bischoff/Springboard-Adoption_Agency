from email.policy import default
from flask_sqlalchemy import SQLAlchemy

BASE_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    # Table's Name
    __tablename__ = "pets"
    
    # Table's Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    # Table Functions
    def image_url(self):
        return self.photo_url or BASE_IMAGE

def connect_db(app):
    db.app = app
    db.init_app(app)