exercises_db = []

def add_exercise(exercise):
    exercises_db.append(exercise)
    return exercise

def get_exercises():
    return list(exercises_db)