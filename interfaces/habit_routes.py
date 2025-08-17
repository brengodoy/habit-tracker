from flask import Blueprint,jsonify,request
from application.create_habit import create_habit
from application.complete_habit import complete_habit
from infrastructure.habit_repository import HabitRepositorySQLite

habit_blueprint = Blueprint('habit_blueprint',__name__)

@habit_blueprint.route("/habits", methods=["POST"])
def create_habit_route():
    data = request.get_json()
    habit_name = data["habit_name"]
    repo = HabitRepositorySQLite()
    habit = create_habit(habit_name,repo)
    return jsonify({
        "id": habit.id, 
		"name": habit.name, 
		"creation_date": habit.creation_date, 
		"completion_history": habit.completion_history.dates,
    })
    
@habit_blueprint.route("/habits", methods = ["GET"])
def get_habits_route():
    repo = HabitRepositorySQLite()
    habits = repo.get_all_habits()
    print(habits)
    return jsonify({
		"habits": [
			{
				"id": h.id,
				"name": h.name,
				"creation_date": h.creation_date,
				"completion_history": h.completion_history,
			}
			for h in habits
		]
	})

@habit_blueprint.route("/habits/<int:habit_id>/complete", methods=["PATCH"])
def complete_habit_route(habit_id):
    repo = HabitRepositorySQLite()
    habit = repo.get_habit_by_id(habit_id)
    complete_habit(habit,repo)
    return jsonify({
		"id": habit.id,
        "name": habit.name,
        "creation_date": habit.creation_date,
        "completion_history": habit.completion_history.dates,
	})
    