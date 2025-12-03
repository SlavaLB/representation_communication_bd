# Нужно для alembic - один импорт который видит все модели сразу

from models.base import Base  # noqa
from models.many_to_many import Country  # noqa
from models.one_to_many import Phone  # noqa
from models.one_to_one import Passport  # noqa
from models.person import Person  # noqa
