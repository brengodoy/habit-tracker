from create_habit import is_name_valid

def edit_habit(new_name: str,habit,habit_repository) -> object:
    if not is_name_valid(new_name):
        raise ValueError("Habit name is not valid.")
    habit.edit_habit_name(new_name)
    habit_repository.save(habit)
    return habit