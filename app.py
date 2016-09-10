from flask import Flask, render_template
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required
from models import User, Role, db

# app setup
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create a user to test with
@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()
    user_datastore.create_user(email='casey@gmail.com', password='password')
    db.session.commit()


@app.route('/')
@login_required
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
