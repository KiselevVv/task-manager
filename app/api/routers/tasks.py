from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.api.exceptions import TASK_NOT_FOUND
from app.api.repositories.task import TaskRepository
from app.api.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskResponse])
async def get_all_tasks(db: AsyncSession = Depends(get_db)) -> List[TaskResponse]:
    """Получает список всех задач."""
    repo = TaskRepository(db)
    return await repo.get_all()


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)) -> TaskResponse:
    """Получает задачу по её ID."""
    repo = TaskRepository(db)
    task = await repo.get_by_id(task_id)
    if not task:
        raise TASK_NOT_FOUND
    return task


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate, db: AsyncSession = Depends(get_db)
) -> TaskResponse:
    """Создаёт новую задачу."""
    repo = TaskRepository(db)
    return await repo.create(task_data.model_dump())


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int, task_data: TaskUpdate, db: AsyncSession = Depends(get_db)
) -> TaskResponse:
    """Создаёт новую задачу."""
    repo = TaskRepository(db)
    task = await repo.update(task_id, task_data.model_dump())
    if not task:
        raise TASK_NOT_FOUND
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)) -> None:
    """Удаляет задачу."""
    repo = TaskRepository(db)
    task = await repo.get_by_id(task_id)
    if not task:
        raise TASK_NOT_FOUND
    await repo.delete(task_id)
