from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Passport(Base):
    """Паспорт (1:1 с Person)"""
    __tablename__ = "passport"

    id = Column(Integer, primary_key=True)
    number = Column(String(50))

    # ForeignKey с UNIQUE для 1:1
    # UNIQUE обеспечивает, что один паспорт принадлежит только одному человеку
    person_id = Column(Integer, ForeignKey("person.id"), unique=True)

    # 1:1 обратно
    person = relationship(
        "Person",
        back_populates="passport",           # Связь с атрибутом 'passport' в модели Person
        uselist=False,                       # Всегда False для отношений 1:1
        # single_parent=True, Паспорт должен иметь одного "родителя" это уже подразумевается при связи 1 к 1
        lazy="select"                        # По умолчанию создается,
                                             # для получения объекта будет выполняться еще один запрос
    )

    def __repr__(self):
        return f"<Passport(id={self.id}, number='{self.number}')>"
