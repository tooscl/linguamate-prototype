import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.config import TOKEN
from bot.handlers import start, help, restart, feedback, echo

# Логирование
logging.basicConfig(level=logging.INFO)

# Создание объектов бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрация хендлеров
async def register_handlers():
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(restart.router)
    dp.include_router(feedback.router)
    dp.include_router(echo.router)

# Регистрация команд для меню
async def set_commands(bot: Bot): # TODO: добавь /about
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/help", description="Список команд"),
        BotCommand(command="/restart", description="Начать все заново"),
        BotCommand(command="/feedback", description="Оставить нам обратную связь😊")
    ]
    await bot.set_my_commands(commands)

# Запуск бота
async def main():
    await register_handlers()
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
