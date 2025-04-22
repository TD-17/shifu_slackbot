import requests

def handle_ping_gin_request():
    api_url = "https://jadepalace.onrender.com/user/ping"

    try:
        response = requests.post(api_url)
        if response.status_code == 200:
            data = response.json()
            return f"Hey there {data['message']}"
        else:
            return f"Failed to fetch data. Status Code: {response.status_code}"

    except Exception as e:
        return f"Error: {str(e)}"
