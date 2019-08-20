import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Y0uW1llN3v3rGu3$$'