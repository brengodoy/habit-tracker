from flask import Flask, jsonify, request
from interfaces.habit_routes import habit_blueprint
from domain.exceptions import CustomError

def create_app():
    app = Flask(__name__)
    app.register_blueprint(habit_blueprint)
    
    @app.errorhandler(CustomError)
    def handle_custom_error(e):
        return jsonify({"error": e.message}), e.status_code
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)