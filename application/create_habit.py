from domain.habit import Habit
from infrastructure.habit_repository import HabitRepositorySQLite

def create_habit(habit_name: str, habit_repository: HabitRepositorySQLite) -> object:
    if not is_name_valid(habit_name):
        raise ValueError("Habit name is not valid.")
    habit = Habit(habit_name)
    habit_repository.save(habit)
    return habit
    
def is_name_valid(name: str) -> bool:
    if not name:
        return False
    if name.isdigit() or name.isspace():
        return False
    return True