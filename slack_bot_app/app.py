from slack_bolt import App
from config.settings import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, PORT
from routes.ping_route import ping_gin_route
from routes.ask_shifu import ask_shifu_something
from routes.register_route import setup_register_route

# import routes.register

# Initialize your app with your bot token and signing secret
app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

ping_gin_route(app)
ask_shifu_something(app)
setup_register_route(app)

# Start an HTTP server on the specified port
if __name__ == "__main__":
    app.start(port=PORT)
