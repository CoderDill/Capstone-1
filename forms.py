from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.fields.simple import HiddenField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField


class UserSignInForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class UserSignUpForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Email()])


class AddBetForm(FlaskForm):
    amt_wagered = IntegerField("Amount", validators=[InputRequired()])
    hidden = HiddenField("hidden")


class AddResultForm(FlaskForm):
    result = StringField("Result", validators=[InputRequired()], render_kw={
                         "placeholder": "Enter won or lost"})
    hidden_result = HiddenField("hidden")
