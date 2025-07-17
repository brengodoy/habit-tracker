def complete_habit(habit,habit_repository):
    if habit.mark_completed_today():        
        habit_repository.save(habit)
        return habit
    else:
        raise ValueError("Habit can only be marked as completed once a day.")