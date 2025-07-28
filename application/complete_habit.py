from infrastructure.habit_repository import HabitRepositorySQLite
from domain.habit import Habit

def complete_habit(habit: Habit, 
                   habit_repository: HabitRepositorySQLite) -> Habit:
    if habit is None:
        raise ValueError("Habit cannot be None.")
    if habit_repository is None:
        raise ValueError("Habit repository cannot be None.")
    
    if habit.mark_completed_today():
        habit_repository.update_completed_habit(habit)
        return habit
    else:
        raise ValueError("Habit can only be marked as completed once a day.")