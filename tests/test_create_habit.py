import pytest
from application.create_habit import create_habit
from infrastructure.habit_repository import HabitRepositorySQLite

@pytest.fixture
def repo():
	return HabitRepositorySQLite(":memory:")

def test_create_habit_correct_name(repo):
    habit_name = 'study'
    habit = create_habit(habit_name,repo)
    assert habit.name == habit_name
    
def test_create_habit_with_valid_mixed_name(repo):
    habit_name = 'drink 2L - water'
    habit = create_habit(habit_name, repo)
    assert habit.name == habit_name
    
def test_create_habit_without_name(repo):
    habit_name = None
    with pytest.raises(ValueError) as exception_info:
        create_habit(habit_name,repo)
    assert "Habit name is not valid." in str(exception_info.value)
    
def test_create_habit_numbers_name(repo):
    habit_name = '12345'
    with pytest.raises(ValueError) as exception_info:
        create_habit(habit_name,repo)
    assert "Habit name is not valid." in str(exception_info.value)
    
def test_create_habit_blank_name(repo):
    habit_name = ''
    with pytest.raises(ValueError) as exception_info:
        create_habit(habit_name,repo)
    assert "Habit name is not valid." in str(exception_info.value)
    
def test_create_habit_saves_to_db(repo):
    habit_name = 'meditate'
    create_habit(habit_name, repo)
    all_habits = repo.get_all_habits()
    assert any(row[1] == habit_name for row in all_habits)