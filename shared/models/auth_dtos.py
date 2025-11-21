from pydantic import BaseModel, EmailStr

from shared.models.jwt_dtos import JwtToken


class UserCredentials(BaseModel):
    user_ulid: str
    email: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class LoginOpenApi(BaseModel):
    username: EmailStr
    password: str


class LoginUserResponse(BaseModel):
    user_credentials: UserCredentials
    token: JwtToken


class RegisterUser(BaseModel):
    email: EmailStr
    password: str
