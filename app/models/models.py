from pydantic import BaseModel


class RegisterUser(BaseModel):
    fullname:str
    email:str
    hashed_password:str