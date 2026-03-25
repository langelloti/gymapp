from fastapi.routing import APIRouter
from schemas.exercise_schema import Exercise
from services.exercise_service import create_exercise as create_exercise_service
from services.exercise_service import list_exercises as list_exercises_service


router = APIRouter(
    prefix="/exercises",
    tags=["exercises"]
)

@router.get("")
def get_exercises():
    return list_exercises_service() #chama a função list_exercises para obter a lista de exercícios e retorna como resposta da API.

@router.post("")
def create_exercise(exercise: Exercise):
    return create_exercise_service(exercise) #não é necessário passar os campos individualmente, o objeto Exercise já tem os campos name, description e muscle_group.