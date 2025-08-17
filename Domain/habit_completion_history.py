from datetime import date

class HabitCompletionHistory:
    def __init__(self,dates=None):
        self.dates = dates or []
        
    def mark_completed(self,date : date) -> bool:
        if date not in self.dates:
            self.dates.append(date)
            return True
        return False
    
    def get_all_completed_dates(self):
	    return self.dates
