import requests
from slack_bolt import App

API_URL = "https://jadepalace.onrender.com/user/chat"


def ask_shifu_something(app: App):

    @app.command("/ask_shifu")
    def handle_get_request(ack, say, command):
        print("Slash command received:", command)
        ack()  # Acknowledge the command immediately

        user_input = command["text"].strip()  # Get the question

        if not user_input:
            say("Please enter a question after the command. Example: `/ask_bot What is AI?`"
               )
            return

        # Send user input to Jade Palace API
        request_data = {"value": user_input}
        try:

            print("hi there")
            response = requests.post(API_URL, json=request_data)

            if response.status_code == 200:
                data = response.json()
                print(data)
                print(request_data)
                reply_message = f"*Question:* {request_data.get('value')}\n*Answer:* {data.get('data', 'No response received')}"
            else:
                reply_message = f"Error: Received {response.status_code} from Jade Palace API."

        except Exception as e:
            reply_message = f"Failed to fetch response: {str(e)}"

        # Send response back to Slack
        say(reply_message)
