from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Items, Users
from market.forms import RegisterForm
from market import db

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(username=form.username.data, email=form.email.data, password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))

    return render_template('register.html', form=form)