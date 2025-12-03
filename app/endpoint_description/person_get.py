from typing import Dict, Any


class EndpointPersonDocs:
    """Класс для хранения документации эндпоинтов"""

    # Документация для get_person_info
    GET_PERSON_INFO = {
        "summary": "Получение человека с паспортом",
        "description": """
        Возвращает информацию о человеке по ID.

        **Особенности:**
        - Загружает данные паспорта через relationship 1:1
        - Использует optimized loading (selectinload)
        - Обрабатывает случаи отсутствия паспорта

        **Параметры:**
        - person_id: ID человека (передается в заголовке Person-ID)

        **Возвращает:**
        - Объект Person с полной информацией
        """,
        "responses": {
            200: {"description": "Успешный ответ"},
            404: {"description": "Человек не найден"},
            400: {"description": "Неверный ID"},
            500: {"description": "Внутренняя ошибка сервера"}
        }
    }

    # Другие эндпоинты можно добавить здесь
    CREATE_PERSON = {
        "summary": "Создание нового человека",
        "description": "...",
        "responses": {...},
        "tags": ["Люди"]
    }
