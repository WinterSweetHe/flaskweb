from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)

bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
db = SQLAlchemy(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


