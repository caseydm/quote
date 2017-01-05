from flask import Flask
from flask_security import SQLAlchemyUserDatastore, user_registered
from quote.config import ProdConfig
from quote import public, dashboard
from quote.extensions import db, mail, security
from quote.security.models import User, Role
from quote.dashboard.models import Category, Duration, Circulation,\
    ImageLocation, ImageSize, Product
from .utils import save_products


# security setup
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


def create_app(config_object=ProdConfig):
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    mail.init_app(app)
    security.init_app(app, user_datastore)
    db.init_app(app)

    @user_registered.connect_via(app)
    def when_user_registered(sender, user, confirm_token):
        """Receive flask-security signal when user registers"""
        role = user_datastore.find_or_create_role('subscriber')
        user_datastore.add_role_to_user(user, role)
        return None

    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(dashboard.views.blueprint)
    return None


app = create_app()

if __name__ == '__main__':
    app.run()
