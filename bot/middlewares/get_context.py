from aiogram import types

from bot.database.session import AsyncSessionLocal
from bot.database.crud import get_messages
from bot.utils.context_to_dialogue import context_to_dialogue

async def get_context(message: types.Message):
    async with AsyncSessionLocal() as db:
        context = context_to_dialogue(await get_messages(db, message.from_user.id))
        print(context)
    return context
