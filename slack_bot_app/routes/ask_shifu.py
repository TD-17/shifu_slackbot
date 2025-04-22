import requests
from slack_bolt import App
from handlers.ask_handler import get_shifu_answer

def register_ask_routes(app: App):
    @app.command("/ask_shifu")
    def handle_ask_shifu(ack, say, command):
        print("Slash command received:", command)
        ack()

        user_input = command["text"].strip()

        if not user_input:
            say("Please enter a question after the command. Example: `/ask_shifu What is AI?`")
            return

        reply_message = get_shifu_answer(user_input)
        say(reply_message)