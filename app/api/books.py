from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookOut, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])


def check_category_exists(db: Session, category_id: Optional[int]) -> None:
    if category_id is not None and crud.get_category(db, category_id) is None:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {category_id} not found",
        )


@router.get("/", response_model=list[BookOut])
def list_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_books(db, category_id=category_id)


@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    check_category_exists(db, data.category_id)
    return crud.create_book(
        db,
        title=data.title,
        price=data.price,
        description=data.description,
        url=data.url,
        category_id=data.category_id,
    )


@router.put("/{book_id}", response_model=BookOut)
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    if crud.get_book(db, book_id) is None:
        raise HTTPException(status_code=404, detail="Book not found")

    fields = data.model_dump(exclude_unset=True) 
    check_category_exists(db, fields.get("category_id"))
    return crud.update_book(db, book_id, **fields)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)