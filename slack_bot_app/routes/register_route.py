from handlers.register_handler import handle_registration_request
from slack_bot_app.app import app


def setup_register_route(app):

    @app.command("/bot_register")
    def handle_bot_register(ack, respond):
        ack()
        handle_registration_request(respond)
