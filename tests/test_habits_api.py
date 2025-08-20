
class TestCreateHabit:
    def test_success(self, client):
        response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "Drink water"
        
    def test_success_mixed_name(self, client):
        response = client.post(
            "/habits", 
            json = {"habit_name": "drink 2L - water"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "drink 2L - water"
        
    def test_no_name(self, client):
        response = client.post("/habits", json = {"habit_name": None})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Habit name is not valid."
        
    def test_numbers_name(self, client):
        response = client.post("/habits", json = {"habit_name": "123"})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Habit name is not valid."
        
    def test_blank_name(self, client):
        response = client.post("/habits", json = {"habit_name": ''})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Habit name is not valid."
        
class TestCompleteHabit:
    def test_success(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_data = create_habit_response.get_json()
        habit_id = habit_data["id"]
        
        complete_habit_response = client.patch(
            f"/habits/{str(habit_id)}/complete"
        )
        assert complete_habit_response.status_code == 200
        data = complete_habit_response.get_json()
        assert data["id"] == habit_id
        
    def test_already_completed_habit(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_data = create_habit_response.get_json()
        habit_id = habit_data["id"]
        
        client.patch(f"/habits/{str(habit_id)}/complete")
        
        complete_habit_response = client.patch(
            f"/habits/{str(habit_id)}/complete"
        )
        assert complete_habit_response.status_code == 400
        data = complete_habit_response.get_json()
        assert "Habit can only be marked as completed once a" in data["error"]
        
    def test_complete_none_habit(self, client):
        response = client.patch("/habits/None/complete")
        assert response.status_code == 404
