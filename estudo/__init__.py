from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)


from estudo.views import homepage

from estudo.models import Contato

# https://github.com/EduardoSilvaDev/flask.git

