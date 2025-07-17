def delete_habit(habit_repository,habit):
    try:
        habit_repository.delete(habit)
        return True
    except Exception as e:
        return({'status':'error','message':f'Could not delete habit: {e}'})