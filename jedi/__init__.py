from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from jedi.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

login_manger = LoginManager()
login_manger.login_view = "users.login"
login_manger.login_message_category = "danger"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from jedi.main.routes import main
    from jedi.users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manger.init_app(app)
    mail.init_app(app)

    return app
