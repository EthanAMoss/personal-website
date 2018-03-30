from flask import Flask
from flask_mail import Mail
from emoss_website import config

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('emoss_website.config')

# Connect to blog database
blog_db = SQLAlchemy(app)

# Initialize mail sender
mail = Mail(app)

from emoss_website import views

__version__ = 0.1
