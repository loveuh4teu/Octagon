from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Book, Category


# ---------- Categories ----------

def create_category(session: Session, title: str) -> Category:
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_category(session: Session, category_id: int) -> Category | None:
    return session.get(Category, category_id)


def get_categories(session: Session) -> list[Category]:
    return list(session.scalars(select(Category).order_by(Category.id)))


def update_category(session: Session, category_id: int, title: str) -> Category | None:
    category = session.get(Category, category_id)
    if category is None:
        return None
    category.title = title
    session.commit()
    session.refresh(category)
    return category


def delete_category(session: Session, category_id: int) -> bool:
    category = session.get(Category, category_id)
    if category is None:
        return False
    session.delete(category)
    session.commit()
    return True


# ---------- Books ----------

def create_book(
    session: Session,
    title: str,
    price,
    description: str | None = None,
    url: str | None = None,
    category_id: int | None = None,
) -> Book:
    book = Book(
        title=title,
        price=price,
        description=description,
        url=url,
        category_id=category_id,
    )
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_book(session: Session, book_id: int) -> Book | None:
    return session.get(Book, book_id)


def get_books(session: Session, category_id: int | None = None) -> list[Book]:
    stmt = select(Book).order_by(Book.id)
    if category_id is not None:
        stmt = stmt.where(Book.category_id == category_id)
    return list(session.scalars(stmt))


def update_book(session: Session, book_id: int, **fields) -> Book | None:
    """Пример: update_book(session, 1, price=500, title="Новое название")"""
    book = session.get(Book, book_id)
    if book is None:
        return None
    allowed = {"title", "description", "price", "url", "category_id"}
    for key, value in fields.items():
        if key in allowed:
            setattr(book, key, value)
    session.commit()
    session.refresh(book)
    return book


def delete_book(session: Session, book_id: int) -> bool:
    book = session.get(Book, book_id)
    if book is None:
        return False
    session.delete(book)
    session.commit()
    return True