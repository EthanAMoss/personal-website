from emoss_website import app

import flask

from flask import render_template, url_for, request, Response


@app.route('/')
def home_page():
    return "Hello, World!"

