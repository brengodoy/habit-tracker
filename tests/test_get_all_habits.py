import pytest
from infrastructure.habit_repository import HabitRepositorySQLite
from application.get_all_habits import get_all_habits
from application.create_habit import create_habit
from domain.exceptions import RepositoryNotFoundError

@pytest.fixture
def repo():
    return HabitRepositorySQLite(':memory:')

def test_success(repo):
    habit = create_habit("Drink water",repo)
    habits = get_all_habits(repo)
    assert any(h.id == habit.id and h.name == habit.name for h in habits)
    
def test_no_repository():
    with pytest.raises(RepositoryNotFoundError) as e:
        get_all_habits(None)
    assert str(e.value) == "Habit repository cannot be None."