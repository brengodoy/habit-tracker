from application.create_habit import is_name_valid
from infrastructure.habit_repository import HabitRepositorySQLite
from domain.exceptions import HabitNameNotValid

def edit_habit(new_name: str, habit: object, habit_repository: HabitRepositorySQLite) -> object:
    if not is_name_valid(new_name):
        raise HabitNameNotValid("Habit name is not valid.")
    habit.edit_habit_name(new_name)
    habit_repository.edit(habit)
    return habit