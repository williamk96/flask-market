from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Items, Users
from market.forms import RegisterForm, LoginForm, PurchaseForm, SellForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market():
    purchase = PurchaseForm()
    sell = SellForm()
    if request.method == "POST":
        #Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Items.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash("Purchase successful!", category="success")
            else:
                flash("Unfortunately, you don't have enough money to purchase that item.", category="danger")
        #Sell Item Logic
        sold_item = request.form.get('sold_item')
        s_item_object = Items.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold: {s_item_object}.", category="success")
            else:
                flash(f"Something went wrong when trying to sell {s_item_object}", category="danger")
        return redirect(url_for('market'))

    if request.method == "GET":
        items = Items.query.filter_by(owner=None)
        owned_items = Items.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase=purchase, owned_items=owned_items, sell=sell)

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
        login_user(user_to_create)
        flash("Registration Successful!", category="success")

        return redirect(url_for('market'))

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("Logout Successful!", category="info")
    return redirect(url_for('home'))
