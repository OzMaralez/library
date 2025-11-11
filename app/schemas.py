from uuid import UUID
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., max_length=200, description="Book title")
    author: str = Field(..., max_length=100, description="The author of the book")
    year: int = Field(..., ge=1000, le=date.today().year, description="Year of publication")


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    title: Optional[str] = Field(None, max_length=200)
    author: Optional[str] = Field(None, max_length=100)
    year: Optional[int] = Field(None, ge=1000, le=date.today().year)


class BookRead(BookBase):
    id: UUID

    class Config:
        orm_mode = True