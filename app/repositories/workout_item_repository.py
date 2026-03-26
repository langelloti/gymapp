workout_items_db = []

def add_workout_item(workout_item):
    workout_items_db.append(workout_item)
    return workout_item

def get_workout_items():
    return list(workout_items_db)