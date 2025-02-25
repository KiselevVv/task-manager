from fastapi import FastAPI
from app.api.routers import tasks
from app.database import create_tables

app = FastAPI()

app.include_router(tasks.router)


@app.on_event("startup")
async def startup():
    await create_tables()
