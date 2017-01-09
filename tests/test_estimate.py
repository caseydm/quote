# -*- coding: utf-8 -*-
"""
    Test estimate workflow
"""
import json


class TestEstimatePages:

    def test_add_estimate_page(self, client_loggedin):
        response = client_loggedin.get('dashboard/estimates/new')
        assert b'<title>New Estimate</title>' in response.data


class TestAddEstimate:

    def test_add_client_api_success(self, client_loggedin):
        data = json.dumps({
            'fname': 'Joe',
            'lname': 'Yang',
            'email': '',
            'phone': ''
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = client_loggedin.post(
            '/api/client',
            data=data,
            headers=headers
        )
        assert response.status_code == 201
        assert b'"fname": "Joe"' in response.data
        assert b'"user_id": 1' and b'"id": 1' in response.data

    def test_add_client_api_unauthorized(self, client):
        data = json.dumps({
            'fname': 'Joe',
            'lname': 'Yang',
            'email': '',
            'phone': ''
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = client.post(
            '/api/client',
            data=data,
            headers=headers
        )
        assert response.status_code == 302
