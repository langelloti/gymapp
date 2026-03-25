from schemas.exercise_schema import Exercise
import repositories.exercise_repository as exercise_repo

def create_exercise(exercise: Exercise):
    exercise_data = {
        "name": exercise.name,
        "description": exercise.description,
        "muscle_group": exercise.muscle_group
    }
    created_exercise = exercise_repo.add_exercise(exercise_data)
    return created_exercise

def list_exercises():
    exercises = exercise_repo.get_exercises()
    return {"exercises": exercises}