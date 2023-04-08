from pathlib import Path
from dotenv import load_dotenv
from market.lib.key import key

path = Path('.')/'.env'
load_dotenv(dotenv_path=path)

r = key()

class config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class dev_config(config):
    name = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db'
    DEBUG = True
    TESTING = True
    SECRET_KEY = str(r.value)

    def __repr__(self):
        return "Development Configuration"


class prod_config(config):
    name = 'production'
    # create a production config here
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bsre-one:12qwaszx!@QWASZX'
    SECRET_KEY = str(r.value)

    def __repr__(self):
        return "Production Configuration"