from schemas.workout_item_schema import WorkoutItem
import repositories.workout_item_repository as workout_item_repo


def create_workout_item(workout_item: WorkoutItem):
    workout_item_data = {
        "workout_plan_name": workout_item.workout_plan_name,
        "exercise_name": workout_item.exercise_name,
        "series": workout_item.series,
        "repetitions": workout_item.repetitions,
        "break_time": workout_item.break_time,
        "order": workout_item.order,
    }
    created_workout_item = workout_item_repo.add_workout_item(workout_item_data)
    return created_workout_item


def list_workout_items():
    workout_items = workout_item_repo.get_workout_items()
    return {"workout_items": workout_items}
