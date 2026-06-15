from fastapi import FastAPI
from .routers import health, rag, orchestrator

app = FastAPI(title="ARLYX Core v2.1")

app.include_router(health.router)
app.include_router(rag.router)
app.include_router(orchestrator.router)
