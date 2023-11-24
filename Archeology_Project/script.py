from flask import Flask, render_template, redirect,url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask Instance
app = Flask(__name__)

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# csrf tokens
app.config['SECRET_KEY'] = "Secret"

#Initialize the db
db = SQLAlchemy(app)

# Create a model
class Users(db.Model):
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    organisation = db.Column(db.String(100), nullable=False)
    affiliation = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    # Create A String
    def __ref__(self):
        return '<Name %r>' % self.firstNsme


# Create a form class
class RegisterForm(FlaskForm):
    firstName = StringField("Enter your First Name", validators=[DataRequired()])
    lastName = StringField("Enter your Last Name", validators=[DataRequired()])
    org = StringField("Enter your Organisation Name", validators=[DataRequired()])
    Affiliation = SelectField(u'Dropdown', 
                    choices=[('K-12 Student', 'K-12 Student'), 
                             ('Undergraduate Student', 'Undergraduate Student'), 
                             ('Graduate student', 'Graduate student'),
                             ('K-12 Teacher', 'K-12 Teacher'),
                             ('Higher Ed. Faculty', 'Higher Ed. Faculty'),
                             ('Independent Researcher', 'Independent Researcher'),
                             ('Public Agency Archeologist', 'Public Agency Archeologist'),
                             ('CRM Form Archeologist', 'CRM Form Archeologist'),
                             ('NonProfessional/Avocational Archeologist', 'NonProfessional/Avocational Archeologist'),
                             ('General Public', 'General Public'),
                             ('Native American/Indigenous researcher', 'Native American/Indigenous researcher')])
    email = StringField("Enter your Email", validators=[DataRequired()])
    password = PasswordField("Enter your Password", validators=[DataRequired(), EqualTo('conPassword', message='Passwords must match')])
    conPassword = PasswordField("Confirm Password", validators=[DataRequired()])
    register = SubmitField("Register")


# Create a route decorator
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    firstName = None
    lastName = None
    org = None
    Affiliation = None
    email = None
    password = None
    conPassword = None
    form = RegisterForm()
    if  form.validate_on_submit():
        firstName = form.firstName.data
        form.firstName.data = ''
        lastName = form.lastName.data
        form.lastName.data = ''
        org = form.org.data
        Affiliation = form.Affiliation.data
        form.Affiliation.data = ''
        email = form.email.data
        form.email.data = ''
        password = form.password.data
        form.password.data = ''
        conPassword = form.conPassword.data
        form.conPassword.data = ''

        flash("Registered Successfully")
    return render_template('register.html', firstName = firstName, form=form)



