from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)

bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

manage = Manager(app)
migrate = Migrate(app, db)

manage.add_command("db1", MigrateCommand)


from .main import main as main_blueprint
from .auth import auth as auth_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')









