from infrastructure.habit_repository import HabitRepositorySQLite
from domain.habit import Habit

def get_habit(habit_id: int,repo: HabitRepositorySQLite) -> Habit:
    return repo.get_habit_by_id(habit_id)
