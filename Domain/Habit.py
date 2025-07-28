from datetime import datetime
from domain.habit_completion_history import HabitCompletionHistory

class Habit():
    def __init__(self,
                 name,
                 habit_id = None,
                 creation_date = None,
                 completion_history = None):
        self.id = habit_id
        self.name = name
        self.creation_date = creation_date or datetime.now()
        self.completion_history = completion_history or HabitCompletionHistory()
        
    def edit_habit_name(self,new_name):
        self.name = new_name
    
    def mark_completed_today(self):
        return self.completion_history.mark_completed(datetime.now().date())