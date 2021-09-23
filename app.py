from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
from models import db, connect_db, User, Bet
from secret import API_KEY
from forms import UserForm

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
    # form = UserForm()
    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "americanfootball_nfl", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    nfl_response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return render_template("home_page.html", nfl_response=nfl_response.json())


@app.route("/accounts")
def accounts():
    return render_template("account_page.html")


@app.route("/sign_in", methods=["POST"])
def logged_in_page():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        print(username)
    return redirect("/")


@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    form = UserForm()
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    print(username, password)
    new_user = User.register(username, password, email)
    db.session.add(new_user)
    db.session.commit()

    return render_template("logged_in.html")
