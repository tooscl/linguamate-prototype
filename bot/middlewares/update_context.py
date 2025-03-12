from aiogram import types

from bot.database.session import AsyncSessionLocal
from bot.database.crud import save_message


async def update_context(message: types.Message, answer: str):
    async with AsyncSessionLocal() as db:
        await save_message(db, message.from_user.id, "user", message.text)
        await save_message(db, message.from_user.id, "assistant", answer)
