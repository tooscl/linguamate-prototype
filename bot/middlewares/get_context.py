from aiogram import types

from bot.database.session import AsyncSessionLocal
from bot.database.crud import get_messages

async def get_context(message: types.Message):
    async with AsyncSessionLocal() as db:
        context = await get_messages(db, message.from_user.id)
    return context
