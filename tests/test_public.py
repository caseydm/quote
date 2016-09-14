def test_public_home_page(testapp):
    """View public home page"""

    response = testapp.get('/')

    assert b'Home Page' in response
