from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Using small database for this flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '52c4e309dc57904c27d3a3cc'  # Secret key is necessary for flask forms to work
app.static_folder = 'static'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from market import routes
