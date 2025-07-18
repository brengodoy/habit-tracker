from infrastructure.habit_repository import HabitRepositorySQLite

def complete_habit(habit: object, habit_repository: HabitRepositorySQLite) -> object:
    if habit.mark_completed_today():        
        habit_repository.save(habit)
        return habit
    else:
        raise ValueError("Habit can only be marked as completed once a day.")