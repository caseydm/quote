import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECURITY_REGISTERABLE = True

# sendgrid setup
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = '587'
MAIL_USE_SSL = False
MAIL_USERNAME = 'apikey'
MAIL_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
