# Связь 1:1 (One-to-One)
# 1. В ОБЕИХ моделях: relationship с uselist=False
#    (чтобы ORM возвращал объект, а не список)
# 2. На стороне "подчинённой" модели: ForeignKey с unique=True
#    (чтобы БД гарантировала уникальность связи)
# 3. Опционально: cascade для управления зависимыми объектами
# 4. Опционально: lazy для контроля загрузки данных

# Связь 1:M (Один ко Многим)
# 1. На стороне "один" (Person): relationship с uselist=True (по умолчанию)
# 2. На стороне "многие" (Phone): ForeignKey к "один"
# 3. БЕЗ unique=True на ForeignKey (иначе будет 1:1)
# 4. back_populates для двусторонней связи
# 5. cascade для управления зависимыми объектами
# 6. Для загрузки многих объектов используйте selectinload (не joined!)

# Связь M:M (Многие ко Многим)
# 1. Создать ассоциативную таблицу (Table, не модель)
# 2. В ОБЕИХ основных моделях: relationship с secondary
# 3. secondary указывает на ассоциативную таблицу
# 4. back_populates для двусторонней связи
# 5. БЕЗ cascade="delete" (иначе удалит связанные объекты!)
# 6. Для загрузки используйте selectinload или joinedload

# Запросы:
# Лучше в запросе явно указывать .options(joinedload()) - joinedload не создает дополнительный запрос
# Жадная загрузка, если описывать в модели, то может быть не очевидно
# Загрузка для M:M (Загружается связанная и от связанной целевая таблица)
# person = session.query(Person).options(
#     selectinload(Person.country_associations).selectinload(PersonCountry.country)
# ).first()

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Person(Base):
    """Человек"""
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # 1:1 - ОДИН паспорт
    passport = relationship(
        "Passport",
        back_populates="person",       # Связь с атрибутом 'person' в модели Passport
        uselist=False,                 # КЛЮЧЕВОЙ ПАРАМЕТР для 1:1.
                                       # Говорит SQLAlchemy, что это один объект, а не список
        cascade="all, delete-orphan",  # Удалит паспорт при удалении человека
        lazy="joined"
    )
    # 1:M - МНОГО телефонов
    phones = relationship(
        "Phone",              # Имя связанной модели
        back_populates="person",       # Атрибут в модели Phone для обратной связи
                                       # По умолчанию uselist=True (список объектов)
        cascade="all, delete-orphan",  # Автоматическое управление телефонами
        lazy='select',                 # Явно указываем (по умолчанию и так 'select')
        order_by="Phone.number"        # Сортировка телефонов (опционально)
    )
    # M:M - МНОГО стран
    # Связь с ассоциативной моделью
    country_associations = relationship(
        "PersonCountry",
        back_populates="person",        # Связь с PersonCountry.person
        cascade="all, delete-orphan"    # Удалит связи при удалении человека
    )

    def __repr__(self):
        return f"<Person(id={self.id}, name='{self.name}')>"
