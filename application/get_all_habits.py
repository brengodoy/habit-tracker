from infrastructure.habit_repository import HabitRepositorySQLite

def get_all_habits(repo: HabitRepositorySQLite):
    return repo.get_all_habits()
    