import os
import socket
import emoss_website.secrets as secrets

# Config Settings
basedir = os.path.abspath(os.path.dirname(__file__))

# Secret Key
SECRET_KEY = secrets.SECRET_KEY

# Mail Configuration
MAIL_SERVER = secrets.MAIL_SERVER
MAIL_PORT = secrets.MAIL_PORT
MAIL_USE_SSL = True
MAIL_USERNAME = secrets.MAIL_USERNAME
MAIL_PASSWORD = secrets.MAIL_PASSWORD
EMAIL_RECIPIENT = secrets.EMAIL_RECIPIENT


# Constants to set
DEFAULT_EMAIL_SUBJECT = "Contact Form Submission"
