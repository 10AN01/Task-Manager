from fastapi import APIRouter,Depends
import datetime
import uuid
from app.models.tablecreate import CreateTasks
router = APIRouter(prefix="/task-manager")#

@router.post("/create-tasks")
def create_task(Tasks:CreateTasks):
    date = datetime.datetime.utcnow()
    unique_id = str(uuid.uuid4())
    taskid = f"taskid{unique_id}_{date.microsecond}_{date.year}"
    Tasks.status = "uncomplete"
    