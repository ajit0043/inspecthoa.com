from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.hoa import get_users, add_user
import json

hoas_views = Blueprint("hoas", __name__)


@hoas_views.route('/hoas', methods=['GET'])
def get_hoas_view():
    users = get_users()
    r = []
    for user in users:
        r.append(user.__dict__)
    return make_response(jsonify({"users": r}), 200)

@hoas_views.route('/hoa/<id>', methods=['GET'])
def get_hoas_view2(id=""):
    if not id:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_id = id

    users = get_users()
    for user in users:
        if str(user.id) ==user_id:
            return make_response(jsonify({"status": "success", "address": user.address}), 200)

    return make_response(jsonify({"status": "Failed", "description": "ID not found"}), 400)


@hoas_views.route('/hoa', methods=['POST'])
def add_hoas_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "user_name" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_name = data["user_name"]

    add_user(user_name)
    return make_response(jsonify({"status": "success"}), 200)
