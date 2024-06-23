from app.utils import load_user_data, save_user_data

def get_all_user_data():
    return load_user_data()

def get_user_profile(user_id):
    user_data = load_user_data()
    return user_data.get(user_id, {})
