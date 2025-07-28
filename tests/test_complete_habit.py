import pytest
from infrastructure.habit_repository import HabitRepositorySQLite
from application.complete_habit import complete_habit
from application.create_habit import create_habit
from datetime import datetime

@pytest.fixture
def repo():
    return HabitRepositorySQLite(':memory:')

@pytest.fixture
def habit(repo):
    return create_habit('Go for a walk',repo)
    
def test_complete_habit_correct(repo,habit):
    dates = complete_habit(habit,repo).completion_history.dates
    assert dates == [datetime.now().date()]
    
def test_already_completed_habit(repo,habit):
    complete_habit(habit,repo)
    with pytest.raises(ValueError) as e:
        complete_habit(habit,repo)
    assert "Habit can only be marked as completed once a day." in str(e.value)

def test_complete_none_habit(repo):
    with pytest.raises(ValueError) as e:
        complete_habit(None,repo)
    assert "Habit cannot be None." in str(e.value)
    
def test_complete_none_repository(habit):
    with pytest.raises(ValueError) as e:
        complete_habit(habit,None)
    assert "Habit repository cannot be None." in str(e.value)
    
def test_complete_habit_saves_in_database(habit,repo):
    complete_habit(habit,repo)
    habit_from_db = repo.get_habit_by_id(habit.id)
    dates_returned = habit_from_db.completion_history.dates
    assert habit_from_db.id == habit.id
    assert habit_from_db.name == habit.name
    assert dates_returned == habit.completion_history.dates
    