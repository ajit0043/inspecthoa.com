from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.user import get_users, add_user
import json

user_views = Blueprint("user", __name__)


@user_views.route('/users', methods=['GET'])
def get_users_view():
    users = get_users()
    r = []
    for user in users:
        r.append(user.__dict__)
    return make_response(jsonify({"users": r}), 200)

@user_views.route('/user/<id>', methods=['GET'])
def get_user_view2(id=""):
    if not id:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_id = id

    users = get_users()
    for user in users:
        if str(user.id) ==user_id:
            return make_response(jsonify({"status": "success", "username": user.username}), 200)

    return make_response(jsonify({"status": "Failed", "description": "ID not found"}), 400)


@user_views.route('/user', methods=['POST'])
def add_user_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "user_name" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_name = data["user_name"]

    add_user(user_name)
    return make_response(jsonify({"status": "success"}), 200)
