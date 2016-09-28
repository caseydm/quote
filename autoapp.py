# -*- coding: utf-8 -*-
"""Create an application instance."""
from quote.app import create_app, db, user_datastore
from quote.config import DevConfig


CONFIG = DevConfig

app = create_app(CONFIG)


@app.before_first_request
def db_setup():
    """Create initial user"""
    db.drop_all()
    db.create_all()
    print('tables created')
    user_datastore.create_user(email='caseym@gmail.com', password='password')
    db.session.commit()
