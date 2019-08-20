from flask import Flask
from config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Y0uW1llN3v3rGu3$$'
app.config.from_object(Config)

from app import routes
