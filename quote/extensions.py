from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask.ext.security import Security
from flask_migrate import Migrate

db = SQLAlchemy()
mail = Mail()
security = Security()
migrate = Migrate()
