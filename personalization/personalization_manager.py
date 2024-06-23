from data.data_manager import get_user_profile
from recommendation.recommender import recommend_items
from text.text_manager import generate_personalized_text

def get_personalized_content(user_id):
    user_profile = get_user_profile(user_id)
    interactions = user_profile.get('interactions', [])

    viewed_items = [interaction['item_id'] for interaction in interactions if interaction['type'] == 'view']
    clicked_items = [interaction['item_id'] for interaction in interactions if interaction['type'] == 'click']
    purchased_items = [interaction['item_id'] for interaction in interactions if interaction['type'] == 'purchase']

    segment = 'browsing'
    if purchased_items:
        segment = 'high_value'
    elif clicked_items:
        segment = 'engaged'
    elif viewed_items:
        segment = 'browsing'

    recommendations = recommend_items(user_id)
    personalized_text = generate_personalized_text(user_profile, segment, recommendations)

    # Adding additional personalization elements
    most_viewed_item = max(viewed_items, key=viewed_items.count) if viewed_items else None
    most_clicked_item = max(clicked_items, key=clicked_items.count) if clicked_items else None

    return {
        'segment': segment,
        'recommendations': recommendations,
        'personalized_text': personalized_text,
        'most_viewed_item': most_viewed_item,
        'most_clicked_item': most_clicked_item
    }
