import datetime

from pydantic import BaseModel


class HealthyStatusModel(BaseModel):
    current_time: datetime.datetime = datetime.datetime.now()
    status: str = "ok"
    code: int = 1
