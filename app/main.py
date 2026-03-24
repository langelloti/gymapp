from fastapi import FastAPI
import api.users_router as users_router   
from api import health

app = FastAPI()
app.include_router(health.router)
app.include_router(users_router.router)