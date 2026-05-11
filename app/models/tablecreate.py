from pydantic import BaseModel

class CreateTasks(BaseModel):
    userid:str
    projectname:str
    taskname:str
    description:str
    priority:str
    status:str