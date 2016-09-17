# -*- coding: utf-8 -*-
"""
    Tests flask-security registration and login functionality
"""
from quote.app import user_datastore


class TestViewPages:
    # view pages
    def test_view_register_page(self, testapp):
        response = testapp.get('/register')
        assert b'Register for an Account' in response

    def test_view_login_page(self, testapp):
        response = testapp.get('/login')
        assert b'Log in' in response

    def test_view_forgot_password_page(self, testapp):
        response = testapp.get('/reset')
        assert b'Recover your Password' in response


class TestRegistration:
    # registration tests
    def test_register_no_password(self, testapp):
        response = testapp.get('/register')

        form = response.form
        form['email'] = 'joe@example.com'
        response = form.submit()

        assert response.status_code == 200
        assert b'Password not provided' in response

    def test_register_no_email(self, testapp):
        response = testapp.get('/register')

        form = response.form
        form['password'] = 'password'
        form['password_confirm'] = 'password'
        response = form.submit()

        assert response.status_code == 200
        assert b'Email not provided' in response

    def test_register_success(self, testapp):
        response = testapp.get('/register')

        form = response.form
        form['email'] = 'joe@example.com'
        form['password'] = 'password'
        form['password_confirm'] = 'password'
        response = form.submit().follow()

        assert response.status_code == 200
        assert b'<title>Dashboard</title>' in response

    def test_user_role_is_subscriber(self, testapp):
        user = user_datastore.get_user('joe@example.com')
        assert user.has_role('subscriber') == True


class TestAnonRedirects:
    def test_dashboard_redirect(self, testapp):
        # try to view dashboard with anonymous user
        response = testapp.get('/dashboard').follow()
        assert b'Please log in to access this page.' in response

    def test_change_password_redirect(self, testapp):
        # try to view change password page with anonymous user
        response = testapp.get('/change').follow()
        assert b'Please log in to access this page.' in response


class TestLogin:
    def test_login_wrong_password(self, testapp):
        response = testapp.get('/login')

        form = response.form
        form['email'] = 'gary@example.com'
        form['password'] = 'wrong_password'
        response = form.submit()

        assert b'Invalid password' in response

    def test_login_correct_password(self, testapp):
        response = testapp.get('/login')

        form = response.form
        form['email'] = 'gary@example.com'
        form['password'] = 'password'
        response = form.submit().follow()

        assert b'<title>Dashboard</title>' in response
