import requests


def handle_ping_gin_request(respond):
    # respond("Pong! HI there!  Gin server is alive and responding.")

    #  URL of the Gin server's /ping endpoint
    url = "http://localhost:8080/user/ping"
    try:
        # Send a GET request to the Gin server's /ping endpoint
        response = requests.get(url)

        # Check if the response is successful
        if response.status_code == 200:
            # Extract and send the JSON response from the Gin server to Slack
            data = response.json()
            message = data.get("message", "No message found")
            respond(f"Gin server says: {message}"
                   )  # Expected output: "Gin server says: pong"
        else:
            # If there's an error, send the status code to Slack
            respond(
                f"Request to Gin server failed with status code: {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        # Catch and respond to any request exceptions
        respond(f"An error occurred: {e}")
