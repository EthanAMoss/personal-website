from emoss_website import app
from datetime import date

from .helper import calculate_age
from .forms import ContactForm

import flask

from flask import render_template, url_for, request, Response


@app.route('/')
def home_page():
    return render_template('home.jinja2.html')


@app.route('/about')
def about_page():
    return render_template('about.jinja2.html',
                           my_age=calculate_age(date(1996, 4, 25)))


@app.route('/blog')
def blog_page():
    return render_template('blog.jinja2.html')


@app.route('/resume')
def resume_page():
    return render_template('resume.jinja2.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        # Send me an email!
        pass

    return render_template('contact.jinja2.html',
                           contact_form=contact_form)
