from fastapi import FastAPI
import api.users_router as users_router   
from api import health
from api import exercise_router

app = FastAPI()
app.include_router(health.router)
app.include_router(users_router.router)
app.include_router(exercise_router.router)


