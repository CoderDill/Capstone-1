from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
from models import db, connect_db, User, Bet
from secret import API_KEY
from forms import UserSignInForm, UserSignUpForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///crappysports_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = API_KEY
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    form_sign_in = UserSignInForm()
    form_sign_up = UserSignUpForm()

    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "americanfootball_nfl", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    nfl_response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return render_template("home_page.html", nfl_response=nfl_response.json(), form_sign_in=form_sign_in, form_sign_up=form_sign_up)


@app.route("/accounts")
def accounts():
    return render_template("account_page.html")


@app.route("/sign_in", methods=["POST", "GET"])
def logged_in_page():
    form = UserSignInForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username)
        print(user)
    return redirect("/")


@app.route("/sign_up", methods=["POST"])
def add_user():
    form = UserSignUpForm()
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    print(username, password)
    new_user = User.register(username, password, email)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")
