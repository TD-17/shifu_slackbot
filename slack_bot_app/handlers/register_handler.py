from slack_bolt import App
import requests

# def handle_registration_request(respond):
#     url = "http://localhost:8080/auth/users/register"

#     registration_data = {
#         "first_name": "shorya",
#         "last_name": "Dixit",
#         "password": "securepassword",
#         "email": "shorya.dixit@gmail.com",
#         "status": True
#     }

#     try:
#         # Send a POST request to the Gin server's /register endpoint
#         print("It was sucessfull..yayayyaya")
#         response = requests.post(url, registration_data)

#         # Check if the response is successful
#         if response.status_code == 200:
#             # Extract and send the JSON response from the Gin server to Slack
#             data = response.json()
#             token = data.get("token", "No token received")
#             respond(f"Registration successful! Token: {token}")
#         else:
#             # If there's an error, send the status code and message to Slack
#             respond(
#                 f"Registration failed with status code: {response.status_code}. "
#                 f"Details: {response.text}")

#     except requests.exceptions.RequestException as e:
#         # Catch and respond to any request exceptions
#         respond(f"An error occurred: {e}")

# Jade Palace API that provides the registration page link
JADE_PALACE_REGISTER_URL = "http://localhost:8080/user/register"


def register_user(app: App):
    # It will handle register command in slack

    @app.command("/register_shifu")
    def handle_register_command(ack, command, say):
        ack()
        user_id = command["user_id"]  #Get slack user_id
        params = {"user_id": user_id}
        print(command)

        try:
            # Request jade palace for registration link
            response = requests.get(JADE_PALACE_REGISTER_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                register_url = data.get("url", "No link receievd")
                say(f"Click here to register: {register_url}")
            else:
                say(f"Failed to fetch registration link. Status: {response.status_code}"
                   )
        except Exception as e:
            say(f"Error fetching registration link: {str(e)}")
