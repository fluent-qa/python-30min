from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
import psycopg
from sqlmodel import SQLModel, Field

pg_url = "postgresql+psycopg://postgres:changeit@127.0.0.1:5432/workspace"
apg_url = "postgresql+psycopg_async://postgres:changeit@127.0.0.1:5432/workspace"

print("create sync engine ........")
engine = create_engine(pg_url, connect_args={'options': '-c search_path=demos,public'})
print(engine)
print("create sync engine --done")

print("create async engine ........")
async_engine = create_async_engine(apg_url, echo=True)
print("create async engine --done")


class DemoHero(SQLModel, table=True):
    __tablename__ = "demo_hero"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

    def to_json(self):
        return self.model_dump()


class DemoUser(SQLModel, table=True, extend_existing=True):
    __tablename__ = "demo_user"
    __table_args__ = {'schema': 'public', 'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    full_name: str


if __name__ == '__main__':
    metadata = SQLModel.metadata
    print(metadata.create_all(engine))
