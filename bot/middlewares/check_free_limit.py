from aiogram import types

from bot.database.session import AsyncSessionLocal
from bot.database.crud import count_messages_today

async def check_free_limit(message: types.Message, limit=10) -> bool:
    async with AsyncSessionLocal() as db:
        return await count_messages_today(db, message.from_user.id) >= limit
