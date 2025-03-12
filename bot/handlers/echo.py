from aiogram import Router, types

from bot.services.chat_ai import get_ai_response
from bot.database.crud import save_message, get_messages
from bot.database.session import AsyncSessionLocal
from bot.middlewares.register_new_user import rergister_user

router = Router()

@router.message()
async def echo(message: types.Message):
    async with AsyncSessionLocal() as db:
        await rergister_user(db, message)
        await save_message(db, message.from_user.id, "user", message.text)
        context = await get_messages(db, message.from_user.id)
    answer = get_ai_response(message.text, context)
    await message.answer(answer)
