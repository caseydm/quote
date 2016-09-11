import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask-security config
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True

# sendgrid setup
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = '587'
MAIL_USERNAME = os.environ.get('SENDGRID_USERNAME')
MAIL_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
