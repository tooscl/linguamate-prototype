from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from bot.database.models import User, Message
from datetime import datetime, timedelta


async def create_user(db: AsyncSession, telegram_id: int, username: str = None, first_name: str = None,
                      last_name: str = None):
    # Проверяем, существует ли пользователь с таким telegram_id
    query = select(User).where(User.telegram_id == telegram_id)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        # Если пользователь существует, возвращаем его
        return existing_user

    # Если пользователя нет, создаем нового
    user = User(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        last_name=last_name
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user(db: AsyncSession, telegram_id: int):
    query = select(User).where(User.telegram_id == telegram_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def save_message(db: AsyncSession, user_id: int, role: str, text: str, ttl_days=1):
    expiration_time = datetime.utcnow() + timedelta(days=ttl_days)
    message = Message(user_id=user_id, role=role, text=text, expiration_time=expiration_time)
    db.add(message)
    await db.commit()
    return message

async def get_messages(db: AsyncSession, user_id: int, limit: int = 10):
    """Получить последние 10 сообщений для треда"""
    query = select(Message).where(Message.user_id == user_id).order_by(Message.timestamp.desc()).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
