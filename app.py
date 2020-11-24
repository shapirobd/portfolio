from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
import os
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "BsMp9293dc!XyZ")

toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/projects')
def show_projects():
    return render_template('projects.html')

@app.route('/contact')
def show_contact():
    return render_template('contact.html')