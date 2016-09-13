from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask.ext.security import Security, SQLAlchemyUserDatastore
from quote.security.models import User, Role


db = SQLAlchemy()
mail = Mail()
security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
