workout_plan_db = []

def add_workout_plan(workout_plan):
    workout_plan_db.append(workout_plan)
    return workout_plan

def get_workout_plans():
    return list(workout_plan_db)