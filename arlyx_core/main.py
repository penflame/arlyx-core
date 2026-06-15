from fastapi import FastAPI
from arlyx_core.router_ingest import router as ingest_router
from arlyx_core.router_query import router as query_router
from arlyx_core.router_health import router as health_router

app = FastAPI(title="ARLYX Core")

app.include_router(ingest_router, prefix="/ingest")
app.include_router(query_router, prefix="/query")
app.include_router(health_router, prefix="/health")
