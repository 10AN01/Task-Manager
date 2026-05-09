from pydantic import BaseModel


class RegisterUser(BaseModel):
    fullname:str
    email:str
    password:str

class LoginUser(BaseModel):
    email:str
    password:str