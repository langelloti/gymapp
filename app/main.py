from fastapi import FastAPI
import api.users_router as users_router   
from api import health
from api import exercise_router
from api import workout_plan_router
from api import workout_item_router

app = FastAPI()
app.include_router(health.router)
app.include_router(users_router.router)
app.include_router(exercise_router.router)
app.include_router(workout_plan_router.router)
app.include_router(workout_item_router.router)
