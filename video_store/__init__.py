from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

from video_store import routes
import os


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
