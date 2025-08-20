
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

class TestDeleteHabit:
    def test_success(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        delete_habit_response = client.delete(f"/habits/{str(habit_id)}")
        assert delete_habit_response.status_code == 200
        message = delete_habit_response.get_json()["message"]
        assert message == f"Habit {str(habit_id)} deleted successfully"
        
    def test_non_existing_habit(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        client.delete(f"/habits/{str(habit_id)}")
        
        delete_habit_response = client.delete(f"/habits/{str(habit_id)}")
        assert delete_habit_response.status_code == 404
        error = delete_habit_response.get_json()["error"]
        assert error == "Habit not found."
        
class TestEditHabit:
    def test_success(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        edit_habit_response = client.patch(
            f"/habits/{str(habit_id)}", 
            json = {"new_name": "Drink juice"}
        )
        assert edit_habit_response.status_code == 200
        edited_habit_data = edit_habit_response.get_json()
        assert edited_habit_data["id"] == habit_id
        assert edited_habit_data["name"] == "Drink juice"
    
    def test_success_mixed_name(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        edit_habit_response = client.patch(
            f"/habits/{str(habit_id)}", 
            json = {"new_name": "drink 2L - water"}
        )
        assert edit_habit_response.status_code == 200
        edited_habit_data = edit_habit_response.get_json()
        assert edited_habit_data["id"] == habit_id
        assert edited_habit_data["name"] == "drink 2L - water"
        
    def test_no_new_name(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        edit_habit_response = client.patch(
            f"/habits/{str(habit_id)}", 
            json = {"new_name": None}
        )
        assert edit_habit_response.status_code == 400
        error = edit_habit_response.get_json()["error"]
        assert error == "Habit name is not valid."
        
    def test_numbers_name(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        edit_habit_response = client.patch(
            f"/habits/{str(habit_id)}", 
            json = {"new_name": "123"}
        )
        assert edit_habit_response.status_code == 400
        error = edit_habit_response.get_json()["error"]
        assert error == "Habit name is not valid."
        
    def test_blank_name(self, client):
        create_habit_response = client.post(
            "/habits", 
            json = {"habit_name": "Drink water"}
        )
        habit_id = create_habit_response.get_json()["id"]
        
        edit_habit_response = client.patch(
            f"/habits/{str(habit_id)}", 
            json = {"new_name": ""}
        )
        assert edit_habit_response.status_code == 400
        error = edit_habit_response.get_json()["error"]
        assert error == "Habit name is not valid."