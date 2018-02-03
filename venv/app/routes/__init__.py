from flask import Flask

__all__ = ['index']

app = Flask(__name__)

from app.routes import *