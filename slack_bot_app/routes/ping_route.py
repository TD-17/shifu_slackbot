import requests
from slack_bolt import App


def ping_gin_route(app: App):

    @app.command("/ping_gin")
    def handle_get_request(ack, body, say):
        ack()  # Acknowledge the command immediately

        # API endpoint to fetch data
        api_url = "http://localhost:8080/user/ping"  # Replace with your actual API

        try:
            response = requests.post(api_url)
            if response.status_code == 200:
                data = response.json()
                message = f"Hey there {data['message']}"
            else:
                message = f"Failed to fetch data. Status Code: {response.status_code}"

        except Exception as e:
            message = f"Error: {str(e)}"

        # Send response back to Slack
        say(message)
