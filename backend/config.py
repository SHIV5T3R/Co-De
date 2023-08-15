"""[General Configuration Params]
"""
import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

    # db config
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT'))

    # Caching Config
    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_DEFAULT_TIMEOUT = os.getenv('CACHE_DEFAULT_TIMEOUT')
    
    # rate limiting requests config
    RATELIMIT_GLOBAL = os.getenv('RATELIMIT_GLOBAL')

    # jwt config
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
    REFRESH_TOKEN_SECRET = os.getenv('REFRESH_TOKEN_SECRET')
    REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES'))


def get_config():
    return Config