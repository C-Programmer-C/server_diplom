from database.auth import create_user
from main import app
from fastapi import Response, status

@app.post("/register")
def register(email: str, password: str, name: str):
    create_user(email, password, name)
    return Response(status_code=status.HTTP_201_CREATED)


@app.post("/login")
def login():
    return {
        "app_name": "123"
    }