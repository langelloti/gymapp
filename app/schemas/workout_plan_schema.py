from pydantic import BaseModel, EmailStr

class WorkoutPlan(BaseModel):
    name: str
    user_email: EmailStr