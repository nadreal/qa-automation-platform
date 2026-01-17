# QA Automation Platform - Demo

**FastAPI backend** for QA automation practice and portfolio purposes. Provides dummy endpoints with in-memory storage to simulate user management and health checks.

## How to Run Localy
**Create and activate Python Virtual Environment**
```bash
python -m venv env
env\Scripts\activate      # Windows
source env/bin/activate   # Linux/Mac
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```
**Run Server**
```bash
uvicorn backend.app.main:app --reload
Server will run at: http://127.0.0.1:8000
```
## Endpoints

- **GET `/health`** – API health check. Returns: {"status": "ok"}

- **POST `/users/`** – Create a new user. Send JSON: 
```json
{
    "id": 1,
    "name": "Stevan",    
    "role": "user"
}
```

- **GET `/users/{id}`** – Get a user by ID. Returns user JSON.


