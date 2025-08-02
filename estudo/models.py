from estudo import db
from datetime import datetime, timezone

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = True)
    subject = db.Column(db.String, nullable = True)
    message = db.Column(db.String, nullable = True)
    response = db.Column(db.Integer, default = 0)
    
    dt_created = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    active = db.Column(db.Boolean, default = True)

