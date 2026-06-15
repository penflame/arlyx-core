from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def query(q: str):
    return {"query": q, "answer": "stub"}
