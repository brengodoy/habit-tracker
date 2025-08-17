import sqlite3
import json
from domain.habit_completion_history import HabitCompletionHistory
from domain.habit import Habit
from datetime import datetime

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
    
    def save(self,habit : object):
        cursor = self.conn.cursor()
        completion_history_json = json.dumps(habit.completion_history.dates)
        habit_data = (habit.name, 
                      habit.creation_date.isoformat(), 
                      completion_history_json)
        sql = '''
				INSERT INTO habit (name, creation_date, completion_history)
				VALUES (?,?,?)
			'''
        cursor.execute(sql, habit_data)
        self.conn.commit()
        habit.id = cursor.lastrowid
    
    def delete(self,habit : object):
        if habit.id is None:
            raise ValueError("Habit must have an ID to be deleted.")
        cursor = self.conn.cursor()
        sql = 'DELETE FROM habit WHERE id = ?'
        cursor.execute(sql,(habit.id,))
        self.conn.commit()
        
    def get_all_habits(self) -> list[any]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM habit')
        rows = cursor.fetchall()
        return [Habit(habit_id=row[0], name=row[1], creation_date=row[2], completion_history=row[3]) for row in rows]
    
    def edit(self,habit : object):
        cursor = self.conn.cursor()
        sql = '''UPDATE habit 
            SET name = ? 
            WHERE id = ?'''
        data = (habit.name,habit.id)
        cursor.execute(sql,data)
        self.conn.commit()
        
    def update_completed_habit(self,habit : object):
        cursor = self.conn.cursor()
        dates_json = json.dumps(
            [date.isoformat() for date in habit.completion_history.dates]
        )
        sql = '''UPDATE habit 
            SET completion_history = ? 
            WHERE id = ?'''
        cursor.execute(sql,(dates_json,habit.id))
        self.conn.commit()
        
    def get_habit_by_id(self, habit_id: int):
        cursor = self.conn.cursor()
        sql = '''SELECT id, name, creation_date, completion_history
                 FROM habit
                 WHERE id = ?'''
        cursor.execute(sql,(habit_id,))
        row = cursor.fetchone()
        
        if row:
            _, name, creation_date, completion_history_json = row
            dates = json.loads(completion_history_json)
            history = HabitCompletionHistory()
            history.dates = [
                datetime.strptime(d, "%Y-%m-%d").date() for d in dates
                ]
            return Habit(name, habit_id, creation_date, history)
        else:
            raise Exception('Habit not found.')
        