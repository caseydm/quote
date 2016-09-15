# -*- coding: utf-8 -*-
"""
    Test public facing web pages (no login)
"""


def test_public_home_page(client):
    response = client.get('/')
    assert b'Home Page' in response.data
