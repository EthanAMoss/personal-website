from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField


class ContactForm(Form):
    name = StringField()
    email = StringField()
    msg_body = TextAreaField()