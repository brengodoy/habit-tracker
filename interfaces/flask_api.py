from flask import Flask, jsonify, request
from interfaces.habit_routes import habit_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(habit_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)