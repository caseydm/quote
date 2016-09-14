import pytest
from quote.config import TestConfig
from quote.app import create_app, user_datastore
from quote.extensions import db as _db
from flask_security.utils import encrypt_password


@pytest.fixture(scope='session')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='session')
def client(request, app):
    """Flask test client"""
    _db.app = app
    with app.app_context():
        _db.create_all()
        user_datastore.create_user(
            email='caseym@gmail.com', password=encrypt_password('password')
        )
        _db.session.commit()

    def teardown():
        _db.session.close()
        _db.drop_all()

    request.addfinalizer(teardown)
    return app.test_client()
