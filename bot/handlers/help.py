from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("""
/start - Выввод стартового сообщения
/help - Выввод команд и их действий
/restart - Обнуление памяти Макса о Вас
/feedback - Оставить обратную связь для нашей команды
""")
