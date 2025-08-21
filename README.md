# 🌸 Habit Tracker API 🌸

> “Building habits, creating change ✨💪”

A **Flask RESTful API** to manage your daily habits.  
Perfect for practicing **backend development**, **testing**, and **Domain-Driven Design (DDD)** principles. 🩷

---

## 💻 Technologies

- Python 3.10.11
- Flask
- SQLite
- Pytest
- JSON for API responses

---

## 📂 Project Structure
```
habit-tracker/
│
├── domain/                  # Entities and exceptions
├── infrastructure/          # Repositories and database
├── application/             # Business logic
├── interfaces/              # Flask API endpoints
└── tests/                   # Unit + Integration tests
```
---

## 🌟 Available Endpoints

| Method | Route           | Description                     |
|--------|----------------|---------------------------------|
| GET    | `/habits`      | Get all habits                  |
| GET    | `/habits/<id>` | Get a habit by ID               |
| POST   | `/habits`      | Create a new habit              |
| PATCH  | `/habits/<id>/complete`      | Complete a habit by ID                  |
| PATCH  | `/habits/<id>`      | Edit a habit by ID                  |
| DELETE  | `/habits/<id>`      | Delete a habit by ID                  |


Example response for `GET /habits`:

```json
[
  {
    "id": 1,
    "name": "Drink water",
    "creation_date": "2025-08-21",
    "completion_history": {
      "dates": ["2025-08-21", "2025-08-22"]
    }
  }
]
```
---

## 🚀 How to Run

1. **Clone the repo:**
```bash
git clone https://github.com/brengodoy/habit-tracker.git
cd habit-tracker
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
python -m interfaces.flask_api
```
---
## 🧪 Tests
Run all tests:
```bash
pytest
```
Includes:
- Unit tests (CRUD habits)
- Integration tests for Flask endpoints
---
## 💖 Author
Brenda – LinkedIn: [Brenda Godoy](https://www.linkedin.com/in/brendagodoy-/)

Project built with ❤️ to practice and showcase backend skills in Python/Flask, with tests and best practices.
