from flask_login import UserMixin

from market.app import app, db, bcrypt, login_manager
from market.lib.get_barcode import barcode

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(
        db.String(length=255),
        nullable=False,
        unique=True
    )
    email = db.Column(db.String(length=255), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    twofa_status = db.Column(
        db.String(length=255),
        db.CheckConstraint(
            'disabled',
            'registered',
            'enabled'),
        nullable=False,
        default='disabled'
    )
    cart = db.Column(db.Integer(), db.ForeignKey('carts.id'))

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'{self.username}'


class Items(db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=24), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    inventory = db.Column(db.Integer())
    cart_id = db.Column(db.Integer(), db.ForeignKey('carts.id'))

    def __repr__(self):
        return f'{self.name}'
    
#    def buy(self, user):
#            self.owner = user.id
#            user.budget -= self.price
#            db.session.commit()

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.barcode = barcode().value
        self.description = description
        self.inventory = 0


class Carts(db.Model):
    __tablename__ = 'Carts'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.relationship('Users', backref='items', lazy=True)
    items = db.relationship('Items', backref='in_cart', lazy=True)