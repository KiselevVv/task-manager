from typing import List, Optional

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task


class TaskRepository:
    """Репозиторий для работы с задачами в базе данных."""

    def __init__(self, db: AsyncSession):
        """Инициализация репозитория."""
        self.db = db

    async def get_all(self) -> List[Task]:
        """Получает все задачи."""
        result = await self.db.execute(select(Task))
        return list(result.scalars().all())

    async def get_by_id(self, task_id: int) -> Optional[Task]:
        """Получает задачу по её ID."""
        result = await self.db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()

    async def create(self, task_data: dict) -> Task:
        """Создаёт новую задачу."""
        new_task = Task(**task_data)
        self.db.add(new_task)
        await self.db.commit()
        await self.db.refresh(new_task)
        return new_task

    async def update(self, task_id: int, task_data: dict) -> Optional[Task]:
        """Обновляет задачу по её ID."""
        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(**task_data)
            .returning(Task.id)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()

        updated_task = result.scalar_one_or_none()
        if updated_task is None:
            return None

        return await self.get_by_id(task_id)

    async def delete(self, task_id: int) -> None:
        """Удаляет задачу по её ID."""
        stmt = delete(Task).where(Task.id == task_id)
        await self.db.execute(stmt)
        await self.db.commit()
