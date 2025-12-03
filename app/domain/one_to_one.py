from typing import Optional, List, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, or_, select, inspect
from sqlalchemy.orm import joinedload

from models import Passport, Person
from schemas.person import PersonResponse


class OneToOne:
    """
    Учебный класс для демонстрации работы с отношением "один к одному" (1:1)
    в SQLAlchemy на примере моделей Person и Passport.

    Отношение 1:1 означает, что:
    - Одна запись в таблице A связана максимум с одной записью в таблице B
    - Одна запись в таблице B связана максимум с одной записью в таблице A

    В нашем примере:
    - Один человек (Person) имеет только один паспорт (Passport)
    - Один паспорт принадлежит только одному человеку
    """

    def __init__(self, session: AsyncSession):
        """
        Инициализация класса с сессией базы данных.

        Args:
            session: Сессия SQLAlchemy для работы с БД
        """
        self.session = session

    async def get_person_by_id(self, person_id: int) -> Optional[PersonResponse]:
        """
            Получение человека по ID с паспортом.
            Используем selectinload для предотвращения N+1 проблемы.
        """
        stmt = select(Person).options(joinedload(Person.passport)).where(and_(Person.id == person_id))

        # Выполняем запрос
        result = await self.session.execute(stmt)
        person = result.scalar_one_or_none()

        inspector = inspect(person)
        all_model_fields = set(inspector.mapper.columns.keys())
        print(f"Все поля модели: {all_model_fields}")
        # {'id', 'name', 'age', 'email', 'password_hash', 'created_at', 'updated_at'}

        # 2. Получаем поля схемы
        schema_fields = set(PersonResponse.model_fields.keys())
        print(f"Поля схемы: {schema_fields}")
        # {'name', 'passport', 'created_at', 'custom_field'}

        # 3. Находим разницу
        excluded_fields = all_model_fields - schema_fields
        print(f"Исключенные поля: {excluded_fields}")
        # {'id', 'age', 'email', 'password_hash', 'updated_at'}

        # 4. Создаем красивую строку
        excluded_str = f"Исключены: {', '.join(sorted(excluded_fields))}"
        print(excluded_str)
        # "Исключены: age, email, id, password_hash, updated_at"

        # 5. Добавляем в custom_field
        person.custom_field = excluded_str
        return person
