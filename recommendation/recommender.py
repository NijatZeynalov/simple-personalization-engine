from data.data_manager import get_all_user_data

def collaborative_filtering(user_id):
    user_data = get_all_user_data()

    # Create a user-item interaction dictionary
    user_item_interactions = {}
    for user, profile in user_data.items():
        user_item_interactions[user] = [interaction['item_id'] for interaction in profile['interactions']]

    # Find users who have similar interactions
    similar_users = {}
    user_items = set(user_item_interactions.get(user_id, []))

    for user, items in user_item_interactions.items():
        if user == user_id:
            continue
        common_items = user_items.intersection(items)
        if common_items:
            similar_users[user] = len(common_items)

    # Get items from similar users that the current user hasn't interacted with
    recommendations = set()
    for similar_user in similar_users:
        items = set(user_item_interactions[similar_user])
        recommendations.update(items - user_items)

    return list(recommendations)

def recommend_items(user_id):
    return collaborative_filtering(user_id)
