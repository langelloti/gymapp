users_db = []

def add_user(user):
    users_db.append(user)
    return user

def get_users():
    return list(users_db)
