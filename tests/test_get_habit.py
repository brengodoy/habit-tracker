import pytest
from infrastructure.habit_repository import HabitRepositorySQLite
from domain.exceptions import RepositoryNotFoundError,HabitNotFoundError
from application.create_habit import create_habit
from application.get_habit import get_habit

@pytest.fixture
def repo():
    return HabitRepositorySQLite(":memory:")

@pytest.fixture
def habit(repo):
    return create_habit("Drink water",repo)

def test_success(habit,repo):
    habit_fetched = get_habit(habit.id,repo)
    assert habit_fetched.id == habit.id
    assert habit_fetched.name == "Drink water"
    
def test_no_repository(habit):
    with pytest.raises(RepositoryNotFoundError) as e:
        get_habit(habit.id,None)
    assert str(e.value) == "Habit repository cannot be None."
    
def test_habit_not_found_when_id_is_none(repo):
    with pytest.raises(HabitNotFoundError) as e:
        get_habit(None,repo)
    assert 'Habit not found' in str(e.value)
    
def test_habit_not_found_for_unknown_id(repo):
    with pytest.raises(HabitNotFoundError) as e:
        get_habit("9999",repo)
    assert 'Habit not found' in str(e.value)