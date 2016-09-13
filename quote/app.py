from flask import Flask
from quote.config import ProdConfig
from quote import public
from .extensions import db, mail, security, user_datastore


def create_app(config_object=ProdConfig):
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    mail.init_app(app)
    security.init_app(app, user_datastore)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    return None

app = create_app()


# Create a user to test with
@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()
    user_datastore.create_user(email='caseym@gmail.com', password='password')
    db.session.commit()


if __name__ == '__main__':
    app.run()
