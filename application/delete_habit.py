from infrastructure.habit_repository import HabitRepositorySQLite
from typing import Union

def delete_habit(habit_repository: HabitRepositorySQLite,habit: object) -> Union[bool, dict]:
    try:
        habit_repository.delete(habit)
        return True
    except Exception as e:
        return({'status':'error','message':f'Could not delete habit: {e}'})