from fastapi import FastAPI

from api import representation_router

app = FastAPI(
    root_path="/api",
    title="Документация по BD",
    description=(
        "Пример как можно описать связи между моделями."
        "Пример запросов к БД."
        "Приложение для более глубокого понимания запросов."
    ),
    version="1.0.0",
)

app.include_router(
    representation_router,
    prefix="/representation",
    tags=["Representation"]
)
