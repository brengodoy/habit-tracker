from datetime import datetime
from domain import HabitCompletionHistory

class Habit():
    def __init__(self,name):
        self.name = name
        self.creation_date = datetime.now()
        self.completion_history = HabitCompletionHistory()
        
    def edit_habit_name(self,new_name):
        self.name = new_name
    
    def mark_completed_today(self):
        return self.completion_history.mark_completed(datetime.now().date())