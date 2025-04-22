import requests

API_URL = "https://jadepalace.onrender.com/user/chat"

def get_shifu_answer(user_input: str) -> str:
    request_data = {"value": user_input}

    try:
        response = requests.post(API_URL, json=request_data)

        if response.status_code == 200:
            data = response.json()
            return f"*Question:* {request_data.get('value')}\n*Answer:* {data.get('data', 'No response received')}"
        else:
            return f"Error: Received {response.status_code} from Jade Palace API."

    except Exception as e:
        return f"Failed to fetch response: {str(e)}"