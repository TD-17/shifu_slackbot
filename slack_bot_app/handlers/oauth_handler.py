import requests
from slack_bolt.app import App
from slack_bolt.oauth.callback_options import CallbackOptions

def handle_oauth_success(request, response):
    installation = request.context.get("installation")
    install_data = installation.to_dict()
    try:
        requests.post("https://jadepalace.onrender.com/slack/store-auth", json=install_data)
        print("✅ Install data sent successfully.")
    except Exception as e:
        print(f"❌ Error sending install data: {e}")
    return response

def handle_oauth_failure(request, response):
    print(f"Request: {request}")
    print(f"Response: {response}")
    response.status = 500
    response.body = "OAuth installation failed."
    return response

def setup_oauth_handlers(app: App):
    app.oauth_flow.callback_options = CallbackOptions(
        success=handle_oauth_success,
        failure=handle_oauth_failure
    )