import requests
from slack_bolt.app import App
from slack_bolt.oauth.callback_options import CallbackOptions
from slack_bolt.response import BoltResponse

def handle_oauth_success(request):
    installation = request.context.get("installation")
    install_data = installation.to_dict()
    try:
        requests.post("https://jadepalace.onrender.com/slack/store-auth", json=install_data)
        print("✅ Install data sent successfully.")
        return BoltResponse(status=200, body="OAuth installation successful.")
    except Exception as e:
        print(f"❌ Error sending install data: {e}")
        return BoltResponse(status=500, body="Failed to store installation data.")

def handle_oauth_failure(request):
    print(f"Request: {request}")
    return BoltResponse(status=500, body="OAuth installation failed.")

def setup_oauth_handlers(app: App):
    app.oauth_flow.callback_options = CallbackOptions(
        success=handle_oauth_success,
        failure=handle_oauth_failure
    )