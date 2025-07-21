import pytest
from infrastructure.habit_repository import HabitRepositorySQLite
from application.create_habit import create_habit
from application.delete_habit import delete_habit
from domain.habit import Habit

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
    fake_habit = Habit('Clean kitchen',None)
    assert delete_habit(repo,fake_habit)['status'] == 'error'
    
def test_delete_habit_db_error(monkeypatch, repo, habit):
    """
    Test that delete_habit returns an error if there is a problem with the database,
    such as a lost connection.
    """
    def fake_delete(_):
        raise Exception("DB connection lost")
    monkeypatch.setattr(repo, "delete", fake_delete)
    result = delete_habit(repo, habit)
    assert result['status'] == 'error'