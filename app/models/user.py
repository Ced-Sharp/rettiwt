from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel, func


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(nullable=False)
    name: str = Field(nullable=False)
    birth_date: date = Field(default=func.now, nullable=False)
    password: str = Field(nullable=False)

