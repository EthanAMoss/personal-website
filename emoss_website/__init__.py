from flask import Flask
from emoss_website import config

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('emoss_website.config')

from emoss_website import views

__version__ = 0.1
