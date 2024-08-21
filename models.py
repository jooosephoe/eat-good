from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    activity_level = db.Column(db.String(1), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

class UserHealth(db.Model):
    __tablename__ = "user_health"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tdee = db.Column(db.Integer)
    calorie_goal = db.Column(db.String(1))
    dietary_pref = db.Column(db.String(20))

    user = db.relationship("User", backref="user_health")

class Allergies(db.Model):
    __tablename__ = "allergies"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    allergy = db.Column(db.String(25))

    user = db.relationship("User", backref="allergies")

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", backref="cart")

class CartItem(db.Model):
    __tablename__ = "cart_item"

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"), nullable=False)
    item = db.Column(db.String(50))

    cart = db.relationship("Cart", backref="cart_item")

class Tracker(db.Model):
    __tablename__ = "tracker"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", backref="tracker")

class TrackerItem(db.Model):
    __tablename__ = "tracker_item"

    id = db.Column(db.Integer, primary_key=True)
    tracker_id = db.Column(db.Integer, db.ForeignKey("tracker.id"), nullable=False)
    item = db.Column(db.String(50))
    meal = db.Column(db.String(1))
    serving_type = db.Column(db.String(2))
    serving_amount = db.Column(db.Integer)