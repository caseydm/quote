def test_public_home_page(client):
    """View public home page"""

    response = client.get('/')

    assert b'Home Page' in response.data
