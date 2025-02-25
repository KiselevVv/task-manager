from fastapi import APIRouter, Depends
from app.api.dependencies import get_db
from app.api.schemas.task import TaskResponse
from app.api.services.task_service import TaskRepository
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskResponse])
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    repo = TaskRepository(db)
    return await repo.get_all()
