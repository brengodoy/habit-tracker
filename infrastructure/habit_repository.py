import sqlite3
import json

class HabitRepositorySQLite():
    def __init__(self,db_path="habits.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
						CREATE TABLE IF NOT EXISTS habit (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						name TEXT,
						creation_date TEXT,
						completion_history TEXT
						)
                    ''')
        self.conn.commit()
    
    def save(self,habit):
        cursor = self.conn.cursor()
        completion_history_json = json.dumps(habit.completion_history.dates)
        habit_data = (habit.name, habit.creation_date.isoformat(), completion_history_json)
        sql = '''
				INSERT INTO habit (name, creation_date, completion_history)
				VALUES (?,?,?)
			'''
        cursor.execute(sql, habit_data)
        self.conn.commit()
        habit.id = cursor.lastrowid
    
    def delete(self,habit):
        if habit.id is None:
            raise ValueError("Habit must have an ID to be deleted.")
        cursor = self.conn.cursor()
        sql = 'DELETE FROM habit WHERE id = ?'
        cursor.execute(sql,(habit.id,))
        self.conn.commit()
        
    def get_all_habits(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM habit')
        return cursor.fetchall()