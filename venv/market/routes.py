from market import app
from flask import render_template
from market.models import Items

@app.route('/')
@app.route('/home')
def home():
    return render_template('bible-study.html')

@app.route('/market')
def market():
    items = Items.query.all()
    return render_template('market.html', items=items)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')