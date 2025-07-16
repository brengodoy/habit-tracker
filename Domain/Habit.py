from datetime import datetime
from domain import HabitCompletionHistory

class Habit():
    def __init__(self,name):
        self.name = name
        self.creation_date = datetime.today()
        self.completion_history = HabitCompletionHistory()
        
    def edit_habit(self,new_name):
        self.name = new_name
    
    def mark_completed_today(self):
        return self.completion_history.mark_completed(datetime.now().date())