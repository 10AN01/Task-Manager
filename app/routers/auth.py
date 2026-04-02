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
    date = datetime.UTCnow()
    insert_user(user_id,user.fullname,user.email,hashed_password,role,date,date)

@router.post("/login")
def login_user(user:LoginUser):
    match = False
    locate_email(user.email)
    password = verify_password(user.password,hashed_password)