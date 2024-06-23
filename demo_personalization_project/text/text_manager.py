def generate_personalized_text(user_data, segment, recommendations):
    name = user_data.get('name', 'User')
    recommendations_str = ', '.join(recommendations)

    message = f"Hello {name}, based on your recent interactions, we have some recommendations for you: {recommendations_str}."

    if segment == 'high_value':
        message += f" Thank you for your purchase! We have selected these premium items just for you."
    elif segment == 'engaged':
        message += f" We noticed you showed interest in similar items. Check these out!"
    elif segment == 'browsing':
        message += f" Here are some products you might find interesting based on your browsing history."

    # Adding more personalized elements
    if 'most_viewed_item' in user_data:
        message += f" By the way, it looks like you have a keen interest in {user_data['most_viewed_item']}."
    if 'most_clicked_item' in user_data:
        message += f" You seem to click a lot on {user_data['most_clicked_item']}."

    return message

