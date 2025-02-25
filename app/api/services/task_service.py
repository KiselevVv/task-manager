from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.task import Task


class TaskRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Task))
        return result.scalars().all()
