from aiogram import Router, types

from bot.services.chat_ai import get_ai_response

router = Router()

@router.message()
async def echo(message: types.Message):
    answer = get_ai_response(message.text)
    await message.answer(answer)
