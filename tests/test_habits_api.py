
class TestCreateHabit:
    def test_success(self,client):
        response = client.post("/habits", json = {"habit_name": "Drink water"})
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "Drink water"
        
    def test_success_mixed_name(self,client):
        response = client.post("/habits", json = {"habit_name": "drink 2L - water"})
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "drink 2L - water"
        
    def test_no_name(self,client):
        response = client.post("/habits", json = {"habit_name": None})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Habit name is not valid."
        
    def test_numbers_name(self,client):
        response = client.post("/habits", json = {"habit_name": "123"})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Habit name is not valid."
        
    def test_blank_name(self,client):
        response = client.post("/habits", json = {"habit_name": ''})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Habit name is not valid."
        