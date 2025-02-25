from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session


async def get_db() -> AsyncSession:
    """
    Генерирует асинхронную сессию базы данных.
    Используется в качестве зависимости для обработки запросов в FastAPI.
    """
    async with async_session() as session:
        yield session
