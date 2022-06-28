import os


class BaseConfig(object):
    ENVIROMENT = os.environ.get('ENVIROMENT')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
