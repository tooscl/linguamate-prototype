from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для моделей
Base = declarative_base()

# Подключение к базе данных
DATABASE_URL = "postgresql+asyncpg://localhost:5433/linguamate"

# Асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=True)

# Сессия
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Создание всех таблиц
async def init_db():
    async with engine.begin() as conn:
        print(f"Подключаемся к адресу: {engine.url}")
        await conn.run_sync(Base.metadata.create_all)

