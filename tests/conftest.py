# -*- coding: utf-8 -*-
"""
    Test fixtures and configuration
"""

import pytest
from webtest import TestApp
from quote.config import TestConfig
from quote.app import create_app, user_datastore
from quote.extensions import db as _db
from flask_security.utils import encrypt_password


@pytest.fixture(scope='class')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='class')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()
        user_datastore.create_user(
            email='gary@example.com', password=encrypt_password('password')
        )
        _db.session.commit()
    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture(scope='class')
def testapp(app, db):
    """A Webtest app."""
    return TestApp(app)


@pytest.fixture(scope='class')
def client(app, db):
    """Flask test client"""
    return app.test_client()


@pytest.fixture(scope='class')
def client_loggedin(app, db):
    client = app.test_client()
    data = dict(email='gary@example.com', password='password', remember='y')
    client.post('/login', data=data)
    return client
