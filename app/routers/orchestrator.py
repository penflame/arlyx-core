from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TaskRequest(BaseModel):
    task: str
    user: str | None = None

@router.post("/orchestrate", tags=["orchestrator"])
def orchestrate(payload: TaskRequest):
    return {
        "task": payload.task,
        "user": payload.user,
        "plan": [],
        "status": "not_implemented"
    }
