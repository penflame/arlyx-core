from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RAGQuery(BaseModel):
    query: str
    user: str | None = None

@router.post("/rag/query", tags=["rag"])
def rag_query(payload: RAGQuery):
    return {
        "query": payload.query,
        "user": payload.user,
        "results": [],
        "status": "not_implemented"
    }
