# App settings and configurations (loads values from environment)
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SLACK_CLIENT_ID = os.environ.get("SLACK_CLIENT_ID")
SLACK_CLIENT_SECRET = os.environ.get("SLACK_CLIENT_SECRET") 
SLACK_REDIRECT_URI = os.environ.get("SLACK_REDIRECT_URI") 
PORT = int(os.environ.get("PORT", 3000))
