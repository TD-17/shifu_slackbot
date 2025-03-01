import requests
from slack_bot_app.config.settings import FASTAPI_SERVER_URL

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
