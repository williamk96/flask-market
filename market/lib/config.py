import os
from pathlib import Path

from dotenv import load_dotenv

from market.lib.key import key

path = Path('.')/'.env'
load_dotenv(dotenv_path=path)

k = key()


class config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Instance-unique settings for security
    INSTANCE_UUID = k.uuid
    INSTANCE_TIMESTAMP = k.timestamp
    SECRET_KEY = k.value
    PASSWORD_SALT = k.salt


class dev_config(config):
    name = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DB_URI")
    DEBUG = True
    TESTING = True

    def __repr__(self):
        return "Development Configuration"


# Base Configuration + Production-specific configuration
class prod_config(config):
    name = 'production'
    # create a production config here
    SQLALCHEMY_DATABASE_URI = os.getenv("PRO_DB_URI")

    def __repr__(self):
        return "Production Configuration"