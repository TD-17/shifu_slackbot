import requests

def handle_oauth_success(args):
    install_data = args.installation.to_dict()
    
    # Send install data to JadePalace backend
    requests.post("https://jadepalace.onrender.com/slack/store-auth", json=install_data)
    
    return "✅ App installed! You can now use /ping_gin or /ask_shifu"