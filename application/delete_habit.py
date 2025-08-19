from infrastructure.habit_repository import HabitRepositorySQLite
from typing import Union
from domain.exceptions import RepositoryNotFoundError,HabitNotFoundError
from domain.habit import Habit

def delete_habit(
    habit_repository: HabitRepositorySQLite, 
    habit: Habit
) -> bool:
    if not habit_repository:
        raise RepositoryNotFoundError("Habit repository cannot be None.")
    
    if not habit:
        raise HabitNotFoundError("Habit cannot be None.")
    
    if habit.id == None:
        raise HabitNotFoundError("Habit ID cannot be None.")
    
    habit_repository.delete(habit)
    return True