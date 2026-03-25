from fastapi.routing import APIRouter
from schemas.user_schema import User
from services.user_service import create_user as create_user_service
from services.user_service import list_users as list_users_service



router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("")
def get_users():
    return list_users_service() #chama a função list_users para obter a lista de usuários e retorna como resposta da API.

@router.post("")
def create_user(user: User):
    return create_user_service(user) #não é necessário passar os campos individualmente, o objeto User já tem os campos name, email e senha.    
