from domain.Habit import Habit

def create_habit(name):
    if not is_name_valid(name):
        raise ValueError("Habit name is not valid.")
    habit = Habit(name)
    #habit_repository.save(habit) de esto se encarga la capa de infraestructura pero no esta definida aun.
    return habit
    
def is_name_valid(name):
    if not name:
        return False
    if name.isdigit() or name.isspace():
        return False
    return True