import os
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.lib.verify_sqlite_db import verify_sqlite_db
from market.lib.config import *
from market.models import *

# add config class here
app_config = dev_config()

app = Flask(__name__)
app.config.from_object(app_config)
print(' * Using {}'.format(app_config))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from market.routes import *

# run some automated checks if using development configuration
if app_config.name == 'development':
    db_path = Path('.')/'market.db'
    if not os.path.isfile(db_path) or not verify_sqlite_db(db_path):
        print(' * Initializing Development Database...')
        db.create_all()
