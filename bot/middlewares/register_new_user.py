from aiogram import types

from bot.database.session import AsyncSessionLocal
from bot.database.crud import get_user, create_user

async def rergister_user(db: AsyncSessionLocal, message = types.Message):
    user = await get_user(db, message.from_user.id)
    if not user:
        await create_user(db, message.from_user.id, message.from_user.username, message.from_user.first_name,
                                     message.from_user.last_name)