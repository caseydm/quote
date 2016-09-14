# view pages
def test_view_register_page(testapp):
    response = testapp.get('/register')

    assert b'Register for an Account' in response


def test_view_login_page(testapp):
    response = testapp.get('/login')

    assert b'Log in' in response


def test_view_forgot_password_page(testapp):
    response = testapp.get('/reset')

    assert b'Recover your Password' in response

# registration tests
def test_register_no_password(testapp):
    response = testapp.get('/register')

    # form = response.forms[]


def test_dashboard_redirect(testapp):
    """Redirect to login page"""
    # try to view dashboard with anonymous user
    response = testapp.get('/dashboard').follow()

    assert b'Log in to your Account' in response