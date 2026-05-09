from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.routers import auth
from app.routers import taskmanager

from app.database.db import create_tasks_table
app = FastAPI()
create_tasks_table()
@app.get("/", response_class=HTMLResponse)
def serve_index():
    return Path("app/index.html").read_text(encoding="utf-8")
app.include_router(auth.router)
app.include_router(taskmanager.router,prefix="/task-manager")

