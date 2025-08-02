from estudo import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = True)
    subject = db.Column(db.String, nullable = True)
    message = db.Column(db.String, nullable = True)
    
    dt_created = db.Column(db.Datetime, default = datetime.datetime.utcnow())
    active = db.Column(db.Boolean, default = True)

