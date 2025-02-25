from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./mydb.db"

engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
