from flask import Flask


def create_app():
    app = Flask(__name__)

    from first_flask.users.views import users

    app.register_blueprint(users)

    return app
