from app import app
from models import User, Bet, db

db.drop_all()
db.create_all()