from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional


class ContactForm(Form):
    contact_name = StringField(u'Your Name', validators=[InputRequired('Please enter your name')],
                               render_kw={'placeholder': 'Name'})
    contact_email = StringField(u'Email Address', validators=[InputRequired('Please enter your email'),
                                                      Email('Please enter a valid email address')],
                                render_kw={'placeholder': 'Email'})
    contact_subject = StringField(u'Subject', validators=[Optional()],
                                  render_kw={'placeholder': 'Subject'})
    contact_message = TextAreaField(u'Message', validators=[InputRequired('Please enter a message')],
                                    render_kw={'placeholder': 'Message'})
