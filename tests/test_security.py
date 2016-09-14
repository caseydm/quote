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
        assert b'<p>Dashboard</p>' in response


class TestAnonRedirects:
    def test_dashboard_redirect(self, testapp):
        """Redirect to login page"""
        # try to view dashboard with anonymous user
        response = testapp.get('/dashboard').follow()

        assert b'Log in to your Account' in response