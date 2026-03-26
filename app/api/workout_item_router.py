from fastapi.routing import APIRouter
from schemas.workout_item_schema import WorkoutItem
from services.workout_item_service import create_workout_item as create_workout_item_service
from services.workout_item_service import list_workout_items as list_workout_items_service

router = APIRouter(
    prefix="/workout_items",
    tags=["workout_items"]
)

@router.get("")
def get_workout_items():
    return list_workout_items_service() #chama a função list_workout_items para obter a lista de itens de treino e retorna como resposta da API.

@router.post("")
def create_workout_item(workout_item: WorkoutItem): 
    return create_workout_item_service(workout_item) #não é necessário passar os campos individualmente, o objeto WorkoutItem já tem os campos workout_plan_name, exercise_name, series, repetitions, break_time e order.