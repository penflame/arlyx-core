from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def ingest_document(doc: str):
    return {"received": len(doc), "status": "ingested"}
