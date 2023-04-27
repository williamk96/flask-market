from pathlib import Path
from dotenv import load_dotenv
from market.lib.key import key

path = Path('.')/'.env'
load_dotenv(dotenv_path=path)

k = key()

# Base configuration
class config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = k.value
    SECURITY_PASSWORD_SALT = k.salt

# Base Configuration + Development-specific configuration
class dev_config(config):
    name = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db'
    DEBUG = True
    TESTING = True

    def __repr__(self):
        return "Development Configuration"


# Base Configuration + Production-specific configuration
class prod_config(config):
    name = 'production'
    # create a production config here
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bsre-one:12qwaszx!@QWASZX'

    def __repr__(self):
        return "Production Configuration"