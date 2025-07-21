import pytest
from infrastructure.habit_repository import HabitRepositorySQLite
from application.edit_habit import edit_habit
from application.create_habit import create_habit

@pytest.fixture
def repo():
    return HabitRepositorySQLite(':memory:')

@pytest.fixture
def habit(repo):
	return create_habit('goforawalk',repo)

def test_edit_habit_correct_name(repo,habit):
    new_name = 'go for a walk'
    edited_habit = edit_habit(new_name, habit, repo)
    assert edited_habit.name == new_name
    
def test_edit_habit_with_valid_mixed_name(repo,habit):
    new_name = 'drink 2L - water'
    edited_habit = edit_habit(new_name, habit, repo)
    assert edited_habit.name == new_name
    
def test_edit_habit_without_name(repo,habit):
    new_name = None
    with pytest.raises(ValueError) as exception_info:
        edit_habit(new_name, habit, repo)
    assert "Habit name is not valid." in str(exception_info.value)
    
def test_edit_habit_numbers_name(repo,habit):
    new_name = '12345'
    with pytest.raises(ValueError) as exception_info:
        edit_habit(new_name, habit, repo)
    assert "Habit name is not valid." in str(exception_info.value)
    
def test_edit_habit_blank_name(repo,habit):
    new_name = ''
    with pytest.raises(ValueError) as exception_info:
        edit_habit(new_name, habit, repo)
    assert "Habit name is not valid." in str(exception_info.value)
    
def test_edit_habit_saves_to_db(repo,habit):
    new_name = 'meditate'
    edit_habit(new_name, habit, repo)
    all_habits = repo.get_all_habits()
    assert any(row[1] == new_name for row in all_habits)