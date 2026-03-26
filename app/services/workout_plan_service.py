from schemas.workout_plan_schema import WorkoutPlan
import repositories.workout_plan_repository as workout_plan_repo

def create_workout_plan(workout_plan: WorkoutPlan):
    workout_plan_data = {
        "name": workout_plan.name,
        "user_email": str(workout_plan.user_email)
    }
    created_workout_plan = workout_plan_repo.add_workout_plan(workout_plan_data)
    return created_workout_plan

def list_workout_plans():
    workout_plan = workout_plan_repo.get_workout_plans()
    return {"workout_plans": workout_plan}   