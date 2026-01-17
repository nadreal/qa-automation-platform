from fastapi import FastAPI
from .routes import admin, users

app = FastAPI(title="QA Automation Demo API")

app.include_router(users.router, prefix="/users")
app.include_router(admin.router, prefix="/admin")

@app.get("/health")
def health():
    return {"status": "ok"}