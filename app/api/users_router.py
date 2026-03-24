from fastapi.routing import APIRouter
from services.user_service import create_user as create_user_service
from schemas.user_schema import User


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("")
def list_users():
    return {"users": []}

@router.post("")
def create_user(user: User):
    return create_user_service(user) #não é necessário passar os campos individualmente, o objeto User já tem os campos name, email e senha.    
