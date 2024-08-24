import other
import models

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import hashlib
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
migrate = Migrate(app, models.db)
secret_key = other.get_api_secret_key
app.config["SECRET_KEY"] = secret_key
db_url = other.get_db_url()
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
models.db.init_app(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return jsonify({"message": "Token is missing"}), 401
        
        try:
            data = jwt.decode(token, secret_key)
            current_user = models.User.query.filter_by(public_id=data["public_id"]).first()
        except:
            return jsonify({"message": "Token is invalid"}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

if __name__ == "__main__":
    app.run(debug = True)