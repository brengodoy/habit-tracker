from datetime import date
from typing import List

def get_habit_history(habit: object) -> List[date]:
    dates = habit.completion_history.get_all_completed_dates()
    if dates:
        return dates
    raise ValueError("This habit has no completed days yet.")