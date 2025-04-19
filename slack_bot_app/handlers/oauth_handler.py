import requests
from slack_bolt.app import App
from slack_bolt.oauth.callback_options import CallbackOptions
from slack_bolt.response import BoltResponse
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def handle_oauth_success(request):
    try:
        # Access installation directly from SuccessArgs
        installation = request.installation
        install_data = installation.to_dict()
        logger.debug(f"Installation data: {install_data}")

        # Make the POST request to store installation data
        response = requests.post(
            "https://jadepalace.onrender.com/slack/store-auth",
            json=install_data,
            timeout=10  # Add a timeout to avoid hanging
        )
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        logger.info("✅ Install data sent successfully.")
        return BoltResponse(status=200, body="OAuth installation successful.")

    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Error sending install data: {e}")
        if isinstance(e, requests.exceptions.HTTPError):
            logger.error(f"HTTP Error response: {e.response.text}")
        return BoltResponse(status=500, body="Failed to store installation data.")

def handle_oauth_failure(request):
    logger.error(f"OAuth failure: {request}")
    return BoltResponse(status=500, body="OAuth installation failed.")

def setup_oauth_handlers(app: App):
    app.oauth_flow.callback_options = CallbackOptions(
        success=handle_oauth_success,
        failure=handle_oauth_failure
    )