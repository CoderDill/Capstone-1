from flask import Flask, request, render_template, redirect, flash, session, jsonify, g
from flask_debugtoolbar import DebugToolbarExtension
import requests
import random
from models import db, connect_db, User, Bet
from forms import UserSignInForm, UserSignUpForm, AddBetForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from threading import Timer
import os


# Get API_KEY & Set current User
API_KEY = os.environ.get('API_KEY')
CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URI', 'postgresql://crappysports_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = API_KEY
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

debug = DebugToolbarExtension(app)


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


def upcoming():
    """Upcoming API DATA"""

    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "upcoming", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    upcoming_response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return upcoming_response


def nfl():
    """NFL API DATA"""

    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "americanfootball_nfl", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    nfl_response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return nfl_response


def mlb():
    """MLB API DATA"""

    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "baseball_mlb", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    mlb_response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return mlb_response


def mma():
    """MMA API DATA"""

    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "mma_mixed_martial_arts", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    mma_response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return mma_response


@app.route("/")
def home_page():
    """Home page."""

    # Forms
    form_sign_in = UserSignInForm()
    form_sign_up = UserSignUpForm()
    form_add_bet = AddBetForm()

    # API Data
    upcoming_response = upcoming()
    nfl_response = nfl()
    mlb_response = mlb()
    mma_response = mma()

    # Check if user is in session, if true, send bets.
    if g.user:
        user_id = g.user.id
        bets = Bet.query.filter_by(user_id=user_id).order_by(Bet.id.desc())
        return render_template("home_page.html",
                               upcoming_response=upcoming_response.json(),
                               nfl_response=nfl_response.json(),
                               mlb_response=mlb_response.json(),
                               mma_response=mma_response.json(),
                               form_sign_in=form_sign_in,
                               form_sign_up=form_sign_up,
                               form_add_bet=form_add_bet,
                               bets=bets)
    return render_template("home_page.html",
                           upcoming_response=upcoming_response.json(),
                           nfl_response=nfl_response.json(),
                           mlb_response=mlb_response.json(),
                           mma_response=mma_response.json(),
                           form_sign_in=form_sign_in,
                           form_sign_up=form_sign_up,
                           form_add_bet=form_add_bet)


@app.route("/sign_in", methods=["POST", "GET"])
def logged_in_page():
    """Logged in home page"""

    form = UserSignInForm()
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        user = User.authenticate(username=username, pwd=password)
        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')
    return redirect("/")


@app.route("/sign_up", methods=["POST"])
def add_user():
    """Signs up a user and adds user to db"""

    form = UserSignUpForm()
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

    if form.validate_on_submit():
        try:
            username = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]

            new_user = User.register(username, password, email)
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            flash("Username already taken or Email already used.", 'danger')
            return render_template("home_page.html")
        do_login(new_user)
        return redirect("/")
    else:
        flash("Information already taken", 'danger')
        return redirect("/")


@app.route("/account")
def accounts():
    """User's account page"""
    user_id = g.user.id
    user = User.query.get(user_id)
    print(user)
    return render_template("account_page.html", user=user)


@app.route("/add_bet", methods=["POST"])
def add_bet():
    """Add a bet"""
    form = AddBetForm()

    # find amount wagered from form data, turn into float
    amt_wagered = "{:.2f}".format(float(request.form["amt_wagered"]))
    float_amt_wagered = float(amt_wagered)

    # get user
    user_id = g.user.id
    user = User.query.get(user_id)

    if float_amt_wagered > user.balance:
        flash("Insufficient funds", 'danger')
        return redirect("/")

    if form.validate_on_submit():

        # Get the hidden tag form data containing [team_1, team_2, bet_odds, name]
        form_data = request.form['hidden']
        bet_data = form_data.split(',')
        bet_odds = bet_data[2]
        float_bet_odds = float(bet_odds)

        # Calculate possible win
        pos_win = ((float_bet_odds * float_amt_wagered) + float_amt_wagered)
        round(pos_win, 2)
        # Take form data & hidden tag data to make new bet
        new_bet = Bet(name=bet_data[3], team_1=bet_data[0], team_2=bet_data[1],
                      amt_wagered=amt_wagered, pos_win=pos_win, user_id=user_id)

        # Take bet amout from user balance
        user.balance = user.balance - float_amt_wagered

        db.session.add(new_bet)

        # logic to automatically determine result by 50/50.
        if bool(random.getrandbits(1)):
            new_bet.result = 'won'
            user.balance = user.balance + pos_win
            db.session.commit()
        else:
            new_bet.result = 'lost'
            db.session.commit()

        db.session.commit()

        return redirect("/")
    return redirect("/")


@app.route("/logout")
def logout():
    """Log a user out"""

    session.pop("curr_user")
    do_logout()
    flash("You have been logged out.", 'success')
    return redirect("/")
