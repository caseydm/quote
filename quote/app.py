from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from quote.config import ProdConfig
from quote import public, dashboard
from quote.extensions import db, mail, security
from quote.security.models import User, Role

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
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(dashboard.views.blueprint)
    return None

app = create_app()


@app.before_first_request
def create_user():
    """Create initial user"""
    db.drop_all()
    db.create_all()
    user_datastore.create_user(email='caseym@gmail.com', password='password')
    db.session.commit()

if __name__ == '__main__':
    app.run()
