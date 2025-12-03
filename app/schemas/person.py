from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


# Базовая модель для человека
class PersonBase(BaseModel):
    # id исключаем из response
    name: str = Field(..., description="Имя человека", examples=["Иван Иванов",])
    # age: Optional[int] = Field(None, description="Возраст человека", examples=[30,])


# Базовая модель для паспорта
# id и person_id исключаем из response
class PassportBase(BaseModel):
    number: str = Field(..., description="Номер паспорта", examples=["4501123456",])


# Модель для ответа с паспортом
class PassportResponse(PassportBase):
    ...


# Полная модель для ответа
class PersonResponse(PersonBase):
    passport: Optional[PassportResponse] = Field(None, description="Данные паспорта, если есть")
    created_at: Optional[datetime] = Field(None, description="Дата создания записи", examples=["2024-01-15T10:30:00",])
    custom_field: str = Field(None, description="Кастомное поле, не из модели", examples=["Пользователь активен",])
