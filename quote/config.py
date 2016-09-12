import os


class Config(object):
    """Base configuration."""
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


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    WTF_CSRF_ENABLED = False  # Allows form testing
