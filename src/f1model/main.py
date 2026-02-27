from fastapi import FastAPI
from f1model.api.v1.router import v1_router

app = FastAPI()
app.include_router(v1_router, prefix="/api/v1")