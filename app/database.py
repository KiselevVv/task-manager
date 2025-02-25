import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
