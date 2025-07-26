from flask import Blueprint, request, jsonify
from utils.storage import save_submission

submit_blueprint = Blueprint('submit', __name__) # create a blueprint called submit_blueprint

@submit_blueprint.route('/submit', methods=['POST']) # using the blueprint, define a route that accepts POST requests
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    success = save_submission(name, email)

    if success:
        return jsonify({"message": "Data saved!"})
    else:
        return jsonify({"error": "Failed to save data"}), 500
