from schemas.user_schema import User
import repositories.user_repository as user_repo

def create_user(user: User):
    user_data = {
        "name": user.name,
        "email": str(user.email)
    }
    created_user = user_repo.add_user(user_data)
    return created_user

def list_users():
    users = user_repo.get_users()
    return {"users": users} 