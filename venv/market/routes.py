from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Items, Users
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('bible-study.html')

@app.route('/market')
def market():
    items = Items.query.all()
    return render_template('market.html', items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash('Login successful!', category='success')
            return redirect(url_for('market'))
        else:
            flash('Either the username or password was incorrect. Please try again.', category='danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(username=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))

    return render_template('register.html', form=form)