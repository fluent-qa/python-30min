from pydantic import BaseModel, Field


class ServerHealthSchema(BaseModel):
    version: str = Field(..., example="1.0.0")
    status: str = Field(..., example="OK")


class Token(BaseModel):
    access_token: str
    refresh_token: str
