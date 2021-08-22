from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Password)

class Bet(db.Model):
    """Bet"""

    __tablename__ = 'bets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_1 = db.Column(db.String(20), nullable=False, unique=True)
    team_2 = db.Column(db.String(20), nullable=False, unique=True)
    amt_wagered = db.Column(db.Float, nullable=False)
    amt_paid = db.Column(db.Float, nullable=False)
    result = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)