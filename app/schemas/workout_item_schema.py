from pydantic import BaseModel, Field

class WorkoutItem(BaseModel):
    workout_plan_name: str = Field(..., description="Name of the workout plan")
    exercise_name: str = Field(..., description="Name of the exercise")
    series: int = Field(..., gt=0, description="Number of series")
    repetitions: int = Field(..., gt=0, description="Number of repetitions")
    break_time: int = Field(..., ge=0, description="Break time in seconds")
    order: int = Field(..., gt=0, description="Order of the exercise in the workout plan")
    


