from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Phone(Base):
    """Телефон (M:1 с Person)"""
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True)
    number = Column(String(50))
    type = Column(String(50))  # "рабочий", "домашний"

    # ForeignKey без UNIQUE (много телефонов у человека)
    person_id = Column(
        Integer,
        ForeignKey("person.id"),
        nullable=False              # Телефон должен принадлежать кому-то (не может быть "сиротой")
    )

    # M:1 обратно
    person = relationship("Person", back_populates="phones")

    def __repr__(self):
        return f"<Phone(id={self.id}, number='{self.number}', type='{self.type}')>"
