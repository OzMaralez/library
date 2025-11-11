from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID

from models import Book
from schemas import BookCreate, BookUpdate


def get_book(
        db: Session,
        book_id: UUID
) -> Optional[Book]:
    return db.query(Book).filter(Book.id == book_id).first()


def list_books(
        db: Session,
        skip: int = 0,
        limit: int = 10
) -> List[Book]:
    statement = select(Book).offset(skip).limit(limit)
    return list(db.execute(statement).scalars())


def create_book(
        db: Session,
        payload: BookCreate
) -> Book:
    new = Book(**payload.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def update_book(
        db: Session,
        book_id: UUID,
        payload: BookUpdate
) -> Optional[Book]:
    obj = get_book(db, book_id)

    if not obj:
        return None

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)
    return obj


def delete_book(
        db: Session,
        book_id: UUID
) -> bool:
    obj = get_book(db, book_id)

    if not obj:
        return False

    db.delete(obj)
    db.commit()
    return True