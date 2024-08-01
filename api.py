import other

from flask import Flask, request, jsonify, make_response
import uuid
import hashlib
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
secret_key = other.get_api_secret_key
app.config["SECRET_KEY"] = secret_key

db = other.connect_to_db()

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
            current_user = None
        except:
            return jsonify({"message": "Token is invalud"}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

if __name__ == "__main__":
    app.run(debug = True)