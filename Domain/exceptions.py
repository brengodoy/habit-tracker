class CustomError(Exception):
    status_code = 400
    
    def __init__(self, message = None):
        super().__init__(message)
        self.message = message or "An error occurred."
        
class HabitNotFoundError(CustomError):
    status_code = 404
    
class RepositoryNotFoundError(CustomError):
    status_code = 500
    
class HabitAlreadyCompletedError(CustomError):
    status_code = 400
    
class HabitNameNotValid(CustomError):
    status_code = 400