from quote.app import create_app
from quote.config import ProdConfig


def test_production_config():
    """Production config."""
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False


def test_require_log_in(client, db, user):
    """Redirect to login page"""
    # try to view home page
    response = client.get('/', follow_redirects=True)

    assert b'Log into' in response.data
