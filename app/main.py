from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.api import books, categories
from app.db.db import engine, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    init_db()
    print("Подключение к БД установлено")
    yield
    engine.dispose()


app = FastAPI(title="Octagon API", lifespan=lifespan)

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}