from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import delete, select, update

from .sessions import Base, session

ModelType = TypeVar("ModelType", bound=Base)


class SynchronizeSessionEnum(BaseModel):
    FETCH = "fetch"
    EVALUATE = "evaluate"
    FALSE = False


class BaseRepo(Generic[ModelType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    async def get_by_id(self, id: int) -> ModelType | None:
        query = select(self.model).where(self.model.id == id)
        return await session.execute(query).scalars().first()

    async def update_by_id(
        self,
        id: int,
        params: dict,
        synchronize_session: SynchronizeSessionEnum = False,
    ) -> None:
        query = (
            update(self.model)
            .where(self.model.id == id)
            .values(**params)
            .execution_options(synchronize_session=synchronize_session)
        )
        await session.execute(query)

    async def delete(self, model: ModelType, session) -> None:
        await session.delete(model)

    async def delete_by_id(
        self,
        id: int,
        synchronize_session: SynchronizeSessionEnum = False,
    ) -> None:
        query = (
            delete(self.model)
            .where(self.model.id == id)
            .execution_options(synchronize_session=synchronize_session)
        )
        await session.execute(query)

    async def save(self, model: ModelType) -> ModelType:
        saved = await session.add(model)
        return saved
