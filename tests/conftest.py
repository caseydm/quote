import pytest
from quote.config import TestConfig
from quote.app import create_app, user_datastore
from quote.models import db as _db
from flask_security.utils import encrypt_password


@pytest.fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """Flask test client"""
    return app.test_client()


@pytest.fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    # .drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    user = user_datastore.create_user(email='caseym@gmail.com', password=encrypt_password('password'))
    db.session.commit()
    return user
