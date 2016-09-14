from quote.app import create_app
from quote.config import ProdConfig
from flask import url_for


def test_production_config():
    """Production config."""
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False


def test_public_home_page(client):
    """View public home page"""

    response = client.get(url_for('public.index'))

    assert b'Home Page' in response.data


def test_dashboard_redirect(client, db, user):
    """Redirect to login page"""
    # try to view dashboard
    response = client.get(url_for('dashboard.index'), follow_redirects=True)

    assert b'Log in' in response.data
