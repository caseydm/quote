def test_public_home_page(testapp):
    """View public home page"""

    response = testapp.get('/')

    assert b'Home Page' in response


def test_dashboard_redirect(testapp):
    """Redirect to login page"""
    # try to view dashboard with anonymous user
    response = testapp.get('/dashboard').follow()

    assert b'Log in to your Account' in response


def test_view_register_page(testapp):
    """View registration page"""
    response = testapp.get('/register')

    assert b'Register for an Account' in response


def test_view_login_page(testapp):
    """View login page"""
    response = testapp.get('/login')

    assert b'Log in' in response
