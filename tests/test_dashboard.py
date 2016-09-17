# -*- coding: utf-8 -*-
"""
    Test dashboard for logged in user
"""


class TestDashboardPages:

    def test_dashboard_index(self, client_loggedin):
        response = client_loggedin.get('/dashboard')
        assert b'gary@example.com' in response.data
