from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database.func_db import init_db


@asynccontextmanager
async def start_app(app: FastAPI):
    print("Приложение запущено")
    await init_db()
    yield
    print("Приложение завершило свою работу")