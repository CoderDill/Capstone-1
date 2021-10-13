"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from app import app
import os
from unittest import TestCase

from models import db, User, Bet

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///crappysports_db_test"


# Now we can import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for bets."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()

        User.query.delete()
        Bet.query.delete()
        
        u0 = User.register("test1", "abc123", "test1@test.com", 500)
        u0.id = 123

        u1 = User.regiu0 = User.register("tester2", "123abc",  "tester2@tester.com")
        u1.id = 456

        db.session.commit()

        u0 = User.query.get(u0.id)
        u1 = User.query.get(u1.id)

        self.u0 = u0
        self.uid0 = u0.id
        self.u1 = u1
        self.uid1 = u1.id

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            username="testuser",
            password="HASHED_PASSWORD",
            email="test@test.com",
        )

        db.session.add(u)
        db.session.commit()

        # User should have no bets
        self.assertEqual(len(u.bets), 0)
        

    def test_user_register(self):
        test_user = User.register("testing", "abc123", "test3@test3.com")
        test_user.id = 1111

        db.session.commit()

        test_user = User.query.get(test_user.id)
        self.assertIsNotNone(test_user)
        self.assertEqual(test_user.username, "testing")
        self.assertEqual(test_user.email, "test3@test3.com")
        self.assertNotEqual(test_user.password, "abc123")
        self.assertTrue(test_user.password.startswith('$2b$'))

    def test_valid_authentication(self):
        u = User.authenticate(self.u0.username, "abc123")
        self.assertIsNotNone(u)
        self.assertEqual(u.id, self.uid0)
