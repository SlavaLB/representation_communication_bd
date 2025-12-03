from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, select
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
            Используем joinedload для предотвращения N+1 проблемы.
        """
        stmt = select(Person).options(joinedload(Person.passport)).where(and_(Person.id == person_id))

        # Выполняем запрос
        result = await self.session.execute(stmt)
        person = result.scalar_one_or_none()

        person.custom_field = "Сюда можно класть свои значения"
        return person

    async def get_person_by_id_without_passport(self, person_id: int) -> Optional[PersonResponse]:
        """
            Получение человека по ID без данных о паспорте.
        """
        stmt = select(Person).where(and_(Person.id == person_id))

        # Выполняем запрос
        result = await self.session.execute(stmt)
        person = result.scalar_one_or_none()

        person.custom_field = "Сюда можно класть свои значения, схема ответа позволит"
        return person
