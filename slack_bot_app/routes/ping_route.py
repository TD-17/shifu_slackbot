from slack_bolt import App
from handlers.ping_handler import handle_ping_gin_request

def register_ping_routes(app: App):
    @app.command("/ping_gin")
    def handle_ping_gin(ack, body, say):
        ack()
        message = handle_ping_gin_request()
        say(message)