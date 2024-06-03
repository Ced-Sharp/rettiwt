from pydantic import BaseModel


class LoginBody(BaseModel):
    email: str
    password: str


class RegisterBody(BaseModel):
    email:str
    name: str
    birthDate: str
    password: str
    confirmPassword: str

