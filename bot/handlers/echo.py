from aiogram import Router, types
from aiogram.utils.chat_action import ChatActionSender
import asyncio

from bot.middlewares.register import register_user
from bot.middlewares.update_context import update_context
from bot.services.chat_ai import get_ai_response
from bot.middlewares.get_context import get_context
from bot.middlewares.check_free_limit import check_free_limit

router = Router()

@router.message()
async def echo(message: types.Message):
    if await check_free_limit(message):
        await message.answer("Mate, you won’t believe it—my phone took a dive straight into my tea. Now it smells like bergamot, but typing’s a no-go for now. Hopefully, it dries out by tomorrow!😅")
        await asyncio.sleep(2)
        await message.answer("Вы уже сегодня отправили n сообщений Максу\n\nЧто бы продолжить сегодня посмотрите рекламу или посмотрите раздел premium!")
        await message.answer_photo(types.FSInputFile("../bot/attachments/kupi-po-bratski.jpeg"))

    else:
        async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
            await asyncio.sleep(2)
            await register_user(message)# Симуляция времени обработки
            context = await get_context(message)
            print(context)
            answer = await get_ai_response(message.text, context)
            await message.answer(answer)
            await update_context(message, answer)