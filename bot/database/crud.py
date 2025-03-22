from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from bot.database.models import User, Message
from datetime import datetime, timedelta, date


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
    """Получить последние 10 сообщений для контекста"""
    query = select(Message.role, Message.text).where(Message.user_id == user_id).order_by(Message.timestamp.desc()).limit(limit)
    result = await db.execute(query)
    return result.all()

async def count_messages_today(db: AsyncSession, user_id: int):
    """Подсчитать количество сообщений пользователя за сегодня"""
    today_start = datetime.combine(date.today(), datetime.min.time())
    query = select(func.count()).where(
        Message.user_id == user_id,
        Message.timestamp >= today_start,
        Message.role == "user"
    )
    result = await db.execute(query)
    return result.scalar()


async def delete_user(db: AsyncSession, user_id: int):
    await db.delete(User).filter(User.telegram_id == user_id)
    await db.commit()

async def delete_user_messages(db: AsyncSession, user_id: int):
    await db.delete(Message).filter(User.telegram_id == user_id)
    await db.commit()
