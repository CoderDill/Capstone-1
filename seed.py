from app import app
from models import User, Bet, db

db.drop_all()
db.create_all()

u1 = User(name='Test User', password='CoolBeans')
u2 = User(name='John Smith', password='HotBeans')

b1 = Bet(team_1="Miami Dolphins", team_2="Arizona Cardinals",
         amt_wagered="100.00",  result="w", amt_paid="210.00", user_id=1)

b2 = Bet(team_1="Miami Dolphins", team_2="Arizona Cardinals",
         amt_wagered="100.00", user_id=2)

db.session.add_all([u1, u2, b1, b2])
db.session.commit()
