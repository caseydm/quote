from flask import url_for


def test_public_home_page(client):
    """View public home page"""

    response = client.get(url_for('public.index'))

    assert b'Home Page' in response.data


def test_dashboard_redirect(client):
    """Redirect to login page"""
    # try to view dashboard
    response = client.get(url_for('dashboard.index'), follow_redirects=True)

    assert b'Log in' in response.data


def test_register_page(client):
    """Redirect to login page"""
    # try to view dashboard
    response = client.get(url_for('dashboard.index'), follow_redirects=True)

    assert b'Log in' in response.data
