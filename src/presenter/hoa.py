from models.hoa import HOA
from typing import List
from repository import hoas



def get_users() -> List[HOA]:
    json_users = hoas.get_hoas()
    users = []
    for json_user in json_users:
        u = HOA(json_user.get("id"), json_user.get("name"), json_user.get("address"))
        users.append(u)
    return users


def add_user(user_name):
    user_id = len(hoas.get_users()) + 1
    new_user = HOA(user_id, user_name)
    user.add_user(new_user)

