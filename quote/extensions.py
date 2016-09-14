from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask.ext.security import Security

db = SQLAlchemy()
mail = Mail()
security = Security()
