from flask import Blueprint, request, jsonify, render_template
from data.data_manager import get_all_user_data
from personalization.personalization_manager import get_personalized_content
from recommendation.recommender import recommend_items
from text.text_manager import generate_personalized_text

bp = Blueprint('main', __name__)

@bp.route('/admin', methods=['GET'])
def admin_panel():
    users = get_all_user_data()
    return render_template('admin.html', users=users)

@bp.route('/personalize', methods=['GET'])
def personalize():
    user_id = request.args.get('user_id')
    content = get_personalized_content(user_id)
    return jsonify(content)

@bp.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    recommendations = recommend_items(user_id)
    return jsonify(recommendations)

@bp.route('/generate_text', methods=['POST'])
def generate_text():
    user_data = request.json
    text = generate_personalized_text(user_data)
    return jsonify({'text': text})
