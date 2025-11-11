from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

import database_repositories as db_repo
from schemas import BookCreate, BookUpdate, BookRead
from database import get_db


router = APIRouter(prefix='/books', tags=["Books"])


@router.post('/', response_model=BookRead, status_code=201)
def create_book(
        payload: BookCreate,
        db: Session = Depends(get_db)
):
    return db_repo.create_book(db, payload)


@router.get('/', response_model=list[BookRead])
def list_books(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, gt=0, le=100),
        db: Session = Depends(get_db)
):
    return db_repo.list_books(db, skip, limit)


@router.get('/{book_id}', response_model=BookRead)
def get_book(
        book_id: UUID,
        db: Session = Depends(get_db)
):
    book = db_repo.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.patch('/{book_id}', response_model=BookRead)
def update_book(
        payload: BookUpdate,
        book_id: UUID,
        db: Session = Depends(get_db)
):
    updated_book = db_repo.update_book(db, book_id, payload)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book


@router.delete('/{book_id}', status_code=204)
def delete_book(
        book_id: UUID,
        db: Session = Depends(get_db)
):
    ok = db_repo.delete_book(db, book_id)

    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")