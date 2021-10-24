from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import backref

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "users"

    @classmethod
    def register(cls, username, pwd, email):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")
        return cls(username=username, password=hashed_utf8, email=email)

    @classmethod
    def authenticate(cls, username, pwd):
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default=1000.00)


class Bet(db.Model):
    """Bet"""

    __tablename__ = "bets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_1 = db.Column(db.String(50), nullable=False)
    team_2 = db.Column(db.String(50), nullable=False)
    amt_wagered = db.Column(db.Float, nullable=False)
    pos_win = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(10), nullable=False, default="pending")
    amt_paid = db.Column(db.Float, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref="bets")
