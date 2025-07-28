from infrastructure.habit_repository import HabitRepositorySQLite
from domain.habit import Habit
from application.complete_habit import complete_habit

repo = HabitRepositorySQLite("habits.db")
repo.create_table()
print("✅ Table created successfully (or already existing).")

habit = Habit("Drink water")
repo.save(habit)
print("✅ ¡Habit saved successfully!")

habit.name = "Drink juice"
repo.edit(habit)
print("✅ ¡Habit updated successfully!")

complete_habit(habit,repo)
print("✅ ¡Habit completed successfully!")

repo.delete(habit)
print("✅ ¡Habit deleted successfully!")

print(f'Habits: \n{repo.get_all_habits()}')