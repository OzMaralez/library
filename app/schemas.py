from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, constr, conint


#Набор ограничений
Title = constr(max_length=200)
Author = constr(max_length=100)
Year = conint(ge=1000, le=date.today().year)



class BookBase(BaseModel):
    title: str = Field(..., max_length=200, description="Book title")
    author: str = Field(..., max_length=100, description="The author of the book")
    year: int = Field(..., ge=1000, le=date.today().year, description="Year of publication")


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True