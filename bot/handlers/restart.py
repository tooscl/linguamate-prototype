from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("restart")) # TODO: /restart
async def cmd_start(message: types.Message):
    await message.answer("""
СДЕЛАЙ ПОДТВЕРЖДЕНИЕ СБРОСА ДАННЫХ, НАСТРОЕК
""")
