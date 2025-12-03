from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "db_communication"
    DB_USER: str = "root"
    DB_PASSWORD: str = ""  # Пустая строка по умолчанию
    DB_DRIVER: str = "mysql+asyncmy"

    @property
    def DATABASE_URL(self) -> str:
        """Строим строку подключения к БД"""
        # Если есть пароль - добавляем его
        if self.DB_PASSWORD:
            return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            # Без пароля (для локальной разработки)
            return f"{self.DB_DRIVER}://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Новый стиль конфига для Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


# Создаем экземпляр настроек
settings = Settings()

# Красивый вывод для проверки
if __name__ == "__main__":
    print("=" * 60)
    print("✅ НАСТРОЙКИ ЗАГРУЖЕНЫ УСПЕШНО")
    print("=" * 60)
    print(f"📦 База данных: {settings.DB_NAME}")
    print(f"👤 Пользователь: {settings.DB_USER}")
    print(f"🔑 Пароль: {'*' * len(settings.DB_PASSWORD) if settings.DB_PASSWORD else '(пустой)'}")
    print(f"🌐 Хост: {settings.DB_HOST}:{settings.DB_PORT}")
    print(f"🔗 URL подключения: {settings.DATABASE_URL}")
    print("=" * 60)
