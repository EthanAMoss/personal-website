from emoss_website import app

import flask

from flask import render_template, url_for, request, Response


@app.route('/')
def home_page():
    return render_template('home.jinja2.html')


@app.route('/about')
def about_page():
    return render_template('about.jinja2.html')


@app.route('/blog')
def blog_page():
    return "Blog: Coming Soon!"


@app.route('/resume')
def resume_page():
    return "Resume: Coming Soon!"


@app.route('/contact')
def contact_page():
    return "Contact Page: Coming Soon!"
