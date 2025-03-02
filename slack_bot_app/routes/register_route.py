from handlers.register_handler import register_user
from slack_bolt import App


def setup_register_route(app: App):
    register_user(app)
