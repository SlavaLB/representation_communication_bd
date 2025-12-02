# Нужно для alembic - один импорт который видит все модели сразу

from app.models.base import Base  # noqa
from app.models.many_to_many import Country  # noqa
from app.models.one_to_many import Phone  # noqa
from app.models.one_to_one import Passport  # noqa
from app.models.person import Person  # noqa
