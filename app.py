from flask import Flask, render_template
from flask_mail import Mail
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required
from models import User, Role, db
from config import ProdConfig

# extensions
mail = Mail()
security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


# app factory
def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    mail.init_app(app)
    security.init_app(app, user_datastore)

    return app

app = create_app()


# Create a user to test with
@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()
    user_datastore.create_user(email='caseym@gmail.com', password='password')
    db.session.commit()


@app.route('/')
@login_required
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
