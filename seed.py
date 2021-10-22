from models import User, Bet
from app import db

db.drop_all()
db.create_all()

u1 = User.register(username='TestUser', pwd='CoolBeans',
                   email="coolbeans@test.com")
u2 = User.register(username='JohnSmith', pwd='HotBeans',
                   email="hotbeans@test.com")

b1 = Bet(team_1="Miami Dolphins", team_2="Arizona Cardinals",
         amt_wagered="100.00",  pos_win="210.00", result="won", amt_paid="210.00", user_id=1)

b2 = Bet(team_1="Miami Dolphins", team_2="Arizona Cardinals",
         amt_wagered="100.00", pos_win="300.00", user_id=1)

db.session.add_all([u1, u2, b1, b2])
db.session.commit()
