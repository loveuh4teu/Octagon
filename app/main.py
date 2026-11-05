from app.db.db import get_session
from app.db import crud


def main():
    with get_session() as session:
        categories = crud.get_categories(session)

        print("=== Категории и книги ===")
        for category in categories:
            print(f"\n[{category.id}] {category.title}")
            for book in crud.get_books(session, category_id=category.id):
                print(f"   - {book.title} | {book.price} руб. | {book.description}")

        print("\n=== Все книги ===")
        for book in crud.get_books(session):
            print(f"{book.id}. {book.title} ({book.category.title}) - {book.price} руб.")


if __name__ == "__main__":
    main()