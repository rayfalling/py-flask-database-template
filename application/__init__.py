from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# creating flask instance
app = Flask(__name__)
bootstrap = Bootstrap(app)

# load configuration
app.config.from_object('configuration')

# handling database
db = SQLAlchemy(app)

from application import router