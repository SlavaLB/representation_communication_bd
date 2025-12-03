from fastapi import FastAPI

from api import representation_router

app = FastAPI(
    root_path="/api",
    title="Документация по BD",
    description=(
        "Пример как можно описать связи между моделями.\n"
        "Пример запросов к БД.\n"
        "Приложение для более глубокого понимания запросов. "
    ),
    version="1.0.0",
)

app.include_router(
    representation_router,
    prefix="/persons",
    tags=["Persons"]
)
