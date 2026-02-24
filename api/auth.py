from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel
from pydantic.networks import EmailStr

from database.auth import authenticate_user, create_user
from utils.auth import create_access_token, create_refresh_token

auth_router = APIRouter()


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@auth_router.post("/register", summary="Create a new user")
def register(data: RegisterRequest):
    is_exist = create_user(data.email, data.password, data.name)
    if not is_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="The user already exists"
        )
    return Response(status_code=status.HTTP_201_CREATED)


@auth_router.post("/login", summary="Create access and refresh tokens for user")
def login(data: LoginRequest):
    user = authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password"
        )
    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }

