from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
from models import db, connect_db, User, Bet
from secret import API_KEY


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///crappysports_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = API_KEY
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():

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


@app.route("/logged_in")
def logged_in_page():
    return render_template()


@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["password"]

    new_user = User.register(username=username, password=password)
    print(new_user.password)

    return redirect("/")
