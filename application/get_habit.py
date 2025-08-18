from infrastructure.habit_repository import HabitRepositorySQLite
from domain.habit import Habit
from domain.exceptions import RepositoryNotFoundError

def get_habit(habit_id: int,repo: HabitRepositorySQLite) -> Habit:
    if repo:
        return repo.get_habit_by_id(habit_id)
    else:
        raise RepositoryNotFoundError("Habit repository cannot be None.")