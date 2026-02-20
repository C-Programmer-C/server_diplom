from pydantic.networks import EmailStr
from database.auth import create_user
from fastapi import Response, status
from pydantic import BaseModel
from fastapi import APIRouter

auth_router = APIRouter()


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@auth_router.post("/register")
def register(data: RegisterRequest):
    is_exist = create_user(data.email, data.password, data.name)
    if not is_exist:
        return Response(status_code=status.HTTP_409_CONFLICT)
    return Response(status_code=status.HTTP_201_CREATED)



@auth_router.post("/login")
def login(data: LoginRequest):
    exist_user = 