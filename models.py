from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(25))

    bets = db.relationship('Bet')


class Bet(db.Model):
    """Bet"""

    __tablename__ = "bets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_1 = db.Column(db.String(20), nullable=False)
    team_2 = db.Column(db.String(20), nullable=False)
    amt_wagered = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(10), nullable=False, default="pending")
    amt_paid = db.Column(db.Float, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User')
