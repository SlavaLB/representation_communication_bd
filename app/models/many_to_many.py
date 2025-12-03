from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


# Ассоциативная таблица
class PersonCountry(Base):
    """Ассоциативная модель"""
    __tablename__ = "person_country"

    person_id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"), primary_key=True)
    visit_date = Column(DateTime)
    purpose = Column(String(50))

    # Отношения к основным моделям
    person = relationship("Person", back_populates="country_associations")
    country = relationship("Country", back_populates="person_associations")

    def __repr__(self):
        return f"<PersonCountry(person_id={self.person_id}, country_id={self.country_id})>"


class Country(Base):
    """Страна (M:M с Person)"""
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # M:M обратно
    # Связь с ассоциативной моделью
    person_associations = relationship(
        "PersonCountry",
        back_populates="country",           # Связь с PersonCountry.country
        cascade="all, delete-orphan"        # Удалит связи при удалении страны
    )

    def __repr__(self):
        return f"<Country(id={self.id}, name='{self.name}')>"
