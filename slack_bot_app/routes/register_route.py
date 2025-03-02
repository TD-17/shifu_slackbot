from handlers.register_handler import register_user
from slack_bot_app.app import app


def setup_register_route(app):
    register_user(app)
