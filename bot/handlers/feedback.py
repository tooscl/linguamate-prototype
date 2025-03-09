from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("feedback")) # TODO: /feedback
async def cmd_start(message: types.Message):
    await message.answer("""
РЕАЛИЗУЙ ФОРМУ СБОРА ОБРАТНОЙ СВЯЗИ
""")
