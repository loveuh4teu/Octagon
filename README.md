# Octagon
# Octagon API

REST API для каталога книг на FastAPI, SQLAlchemy и PostgreSQL.

## Возможности

- CRUD для категорий (`/categories`) и книг (`/books`)
- Фильтр книг по категории: `/books/?category_id=1`
- Проверка существования категории при создании и изменении книги
- Проверка работоспособности: `/health`

## Запуск

1. Установить PostgreSQL в WSL и создать пользователя и базу:
   ```bash
   service postgresql start
   su - postgres -c "psql -c \"CREATE USER octagon WITH PASSWORD '12345';\""
   su - postgres -c "psql -c 'CREATE DATABASE octagon_db OWNER octagon;'"
   ```
2. Создать файл `.env` в корне проекта:
   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=octagon_db
   DB_USER=octagon
   DB_PASSWORD=12345
   ```
3. Создать окружение и установить зависимости:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. (Необязательно) заполнить базу тестовыми данными:
   ```bash
   python -m app.init_db
   ```
5. Запустить API из корня проекта:
   ```bash
   uvicorn app.main:app --reload
   ```

Swagger-документация: http://127.0.0.1:8000/docs

## Эндпоинты

| Метод | Путь | Описание |
|---|---|---|
| GET | `/health` | проверка, что сервис жив |
| GET, POST | `/categories/` | список, создание |
| GET, PUT, DELETE | `/categories/{id}` | получение, изменение, удаление |
| GET, POST | `/books/` | список (`?category_id=`), создание |
| GET, PUT, DELETE | `/books/{id}` | получение, изменение, удаление |

## Структура проекта

```
app/
├── main.py          # точка входа FastAPI
├── schemas.py       # Pydantic-схемы
├── init_db.py       # наполнение базы тестовыми данными
├── api/             # роутеры books.py, categories.py
└── db/              # db.py, models.py, crud.py
```

## Скриншоты

Документация Swagger:
![docs](examples/docs.png)

Результат `GET /books`:
![get books](examples/get_books.png)

Проверка в PostgreSQL:
![psql](examples/psql.png)