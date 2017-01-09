from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_security import Security
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
mail = Mail()
security = Security()
migrate = Migrate()
csrf = CSRFProtect()
