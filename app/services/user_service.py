from schemas.user_schema import User


def create_user(user: User):
    return {"name": user.name, "email": user.email}
