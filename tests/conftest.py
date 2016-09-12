import pytest
from quote.config import TestConfig
from quote.app import create_app


@pytest.fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()
