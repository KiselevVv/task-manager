from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.task import Base

DATABASE_URL = "sqlite+aiosqlite:///./mydb.db"

engine = create_async_engine(DATABASE_URL,
                             connect_args={"check_same_thread": False})
async_session = sessionmaker(engine, expire_on_commit=False,
                             class_=AsyncSession)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
