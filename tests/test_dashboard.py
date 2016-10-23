# -*- coding: utf-8 -*-
"""
    Test dashboard for logged in user
"""


class TestDashboardPages:

    def test_dashboard_index(self, client_loggedin):
        response = client_loggedin.get('/dashboard')
        assert b'gary@example.com' in response.data

    def test_dashboard_new_client_page(self, client_loggedin):
        response = client_loggedin.get('/dashboard/clients/new')
        assert b'<h2>New Client</h2>' in response.data

class TestDashboardNewClient:

    def test_dashboard_add_client(self, client_loggedin):

        rv = client_loggedin.post('/dashboard/clients/new', data=dict(
            fname='Joe',
            lname='Yang',
            email='joe@example.com'
            ), follow_redirects=True)

        assert b'Client saved' in rv.data