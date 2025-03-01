from bot import app


# New functionality
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        client.views_publish(
            # The user that opened your app's app home
            user_id=event["user"],
            # The view object that appears in the app home
            view={
                "type":
                    "home",
                "callback_id":
                    "home_view",
                # Body of the view
                "blocks": [{
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Welcome to your _App's Home tab_* :tada:"
                    }
                }, {
                    "type": "divider"
                }, {
                    "type": "section",
                    "text": {
                        "type":
                            "mrkdwn",
                        "text":
                            "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`."
                    }
                }, {
                    "type":
                        "actions",
                    "elements": [{
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Click me!"
                        }
                    }]
                }]
            })
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
