import models
import other
from flask import Flask
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)

db_url = other.get_db_url()
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

models.db.init_app(app)

with app.app_context():
    if not database_exists(db_url):
        create_database(db_url)
    
    models.db.create_all()