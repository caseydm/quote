from quote.app import create_app
from quote.config import ProdConfig


def test_production_config():
    """Production config."""
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False
