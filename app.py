from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# app setup
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
