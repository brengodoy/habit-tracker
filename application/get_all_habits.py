from infrastructure.habit_repository import HabitRepositorySQLite
from domain.exceptions import RepositoryNotFoundError

def get_all_habits(repo: HabitRepositorySQLite):
    if not repo:
        raise RepositoryNotFoundError("Habit repository cannot be None.")
    
    return repo.get_all_habits()
    