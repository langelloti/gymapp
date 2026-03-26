from fastapi.routing import APIRouter
from schemas.workout_plan_schema import WorkoutPlan
from services.workout_plan_service import create_workout_plan as create_workout_plan_service
from services.workout_plan_service import list_workout_plans as list_workout_plans_service

router = APIRouter(
    prefix="/workout_plans",
    tags=["workout_plans"]
)

@router.get("")
def get_workout_plans():
    return list_workout_plans_service() #chama a função list_workout_plans para obter a lista de planos de treino e retorna como resposta da API.   

@router.post("")
def create_workout_plan(workout_plan: WorkoutPlan):
    return create_workout_plan_service(workout_plan) #não é necessário passar os campos individualmente, o objeto WorkoutPlan já tem os campos name, description e exercises.