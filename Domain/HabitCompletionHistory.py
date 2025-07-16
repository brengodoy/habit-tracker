class HabitCompletionHistory:
    def __init__(self):
        self.dates = []
        
    def mark_completed(self,date):
        if date not in self.dates:
            self.dates.append(date)
            return True
        return False
    
    # def was_completed_on(self, date):
    # 	return date in self.dates