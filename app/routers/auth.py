from fastapi import APIRouter,HTTPException
import uuid
import datetime

from app.models.models import RegisterUser,LoginUser
from app.database.db import insert_user,locate_email
from app.security.hashing import hash_password,verify_password

router = APIRouter(prefix="/auth")

@router.post("/register")
def register_user(user:RegisterUser):
    user_id = str(uuid.uuid4())
    hashed_password = hash_password(user.password)
    role = "user"
    date = datetime.datetime.utcnow()
    insert_user(user_id,user.fullname,user.email,hashed_password,role,date,date)

@router.post("/login")
def login_user(user:LoginUser):
# Finds the column where email exist
    user_email = locate_email(user.email)
    if user_email:
# Gets the password and compares
        hashed_password = user_email[3]
        password = verify_password(user.password,hashed_password)
        if password:
            return {"message":"Successfully logged in!"}
        else:
            raise HTTPException(status_code=401,detail="Invalid password")
        
    else:
        raise HTTPException(status_code=404,detail = "Account don't exist.")
        