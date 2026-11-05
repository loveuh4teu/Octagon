from app.db.db import init_db, get_session
from app.db import crud


def fill_db():
    init_db() 

    with get_session() as session:
        if crud.get_categories(session):
            print("База уже заполнена, пропускаю.")
            return

        fantasy = crud.create_category(session, "Фантастика")
        detective = crud.create_category(session, "Детективы")

        crud.create_book(session, "Дюна", 750,
                         description="Роман Фрэнка Герберта о пустынной планете Арракис",
                         category_id=fantasy.id)
        crud.create_book(session, "Основание", 620,
                         description="Цикл Айзека Азимова о падении Галактической империи",
                         category_id=fantasy.id)
        crud.create_book(session, "Солярис", 540,
                         description="Роман Станислава Лема о загадочном океане",
                         category_id=fantasy.id)

        crud.create_book(session, "Убийство в Восточном экспрессе", 480,
                         description="Классический детектив Агаты Кристи",
                         category_id=detective.id)
        crud.create_book(session, "Собака Баскервилей", 450,
                         description="Приключение Шерлока Холмса",
                         category_id=detective.id)

        print("Данные добавлены.")


if __name__ == "__main__":
    fill_db()