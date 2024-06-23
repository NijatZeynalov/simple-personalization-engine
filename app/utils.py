import json

USER_DATA_FILE = 'data/user_data.json'

def load_user_data():
    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)

def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def format_response(data):
    return {"status": "success", "data": data}
