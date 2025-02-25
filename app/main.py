from fastapi import FastAPI
from app.api.routers import tasks


app = FastAPI()

app.include_router(tasks.router)
