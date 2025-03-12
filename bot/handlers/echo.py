from aiogram import Router, types
from aiogram.utils.chat_action import ChatActionSender
import asyncio

from bot.middlewares.register import register_user
from bot.middlewares.update_context import update_context
from bot.services.chat_ai import get_ai_response
from bot.middlewares.get_context import get_context

router = Router()

@router.message()
async def echo(message: types.Message):
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        await asyncio.sleep(2)
        await register_user(message)# Симуляция времени обработки
        context = await get_context(message)
        print(context)
        answer = get_ai_response(message.text, context)
        await message.answer(answer)
        await update_context(message, answer)