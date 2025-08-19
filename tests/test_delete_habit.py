import pytest
from infrastructure.habit_repository import HabitRepositorySQLite
from application.create_habit import create_habit
from application.delete_habit import delete_habit
from domain.habit import Habit
from domain.exceptions import HabitNotFoundError

@pytest.fixture
def repo():
    return HabitRepositorySQLite(':memory:')

@pytest.fixture
def habit(repo):
    return create_habit('Clean bedroom',repo)

def test_delete_habit(repo,habit):
    delete_habit(repo,habit)
    all_habits = repo.get_all_habits()
    assert all(habit_tuple[1] != 'Clean bedroom' for habit_tuple in all_habits)
    
def test_delete_non_existing_habit(repo):
    fake_habit = Habit(name='Clean kitchen',habit_id=None)
    with pytest.raises(HabitNotFoundError) as e:
        delete_habit(repo,fake_habit)
    assert "Habit ID cannot be None." in str(e.value)
    
def test_delete_habit_db_error(monkeypatch, repo, habit):
    """
    Test that delete_habit returns an error if there is a problem with the database,
    such as a lost connection.
    """
    def fake_delete(_):
        raise Exception("DB connection lost")
    monkeypatch.setattr(repo, "delete", fake_delete)
    
    with pytest.raises(Exception) as e:
        delete_habit(repo, habit)
    assert "DB connection lost" in str(e.value)