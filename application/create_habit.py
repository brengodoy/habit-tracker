from domain.habit import Habit

def create_habit(name,habit_repository):
    if not is_name_valid(name):
        raise ValueError("Habit name is not valid.")
    habit = Habit(name)
    habit_repository.save(habit)
    return habit
    
def is_name_valid(name):
    if not name:
        return False
    if name.isdigit() or name.isspace():
        return False
    return True