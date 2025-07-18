from infrastructure.habit_repository import HabitRepositorySQLite
from domain.habit import Habit

repo = HabitRepositorySQLite("habits.db")
repo.create_table()
print("✅ Table created successfully (or already existing).")

habit = Habit("Drink water")
repo.save(habit)
print("✅ ¡Habit saved successfully!")

repo.delete(habit)
print("✅ ¡Habit deleted successfully!")

print(f'Habits: \n{repo.get_all_habits()}')