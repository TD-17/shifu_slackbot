from slack_bolt.oauth.oauth_settings import OAuthSettings
from handlers.oauth_handler import handle_oauth_success
from config.settings import SLACK_CLIENT_ID, SLACK_CLIENT_SECRET

def get_oauth_settings():
    return OAuthSettings(
        client_id=SLACK_CLIENT_ID,
        client_secret=SLACK_CLIENT_SECRET,
        scopes=["commands", "chat:write", "users:read"],
        installation_store=None,
        state_store=None,
        redirect_uri="https://shifu-slackbot.onrender.com/slack/oauth_redirect",
        install_path="/slack/install",
        redirect_uri_path="/slack/oauth_redirect",
    )