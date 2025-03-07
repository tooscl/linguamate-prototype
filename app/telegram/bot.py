import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from app.config import TOKEN

import app.telegram.messages as msg

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
# Работа с командами
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(msg.start)

@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer(msg.help)

@dp.message(Command("restart"))
async def cmd_start(message: types.Message):
    await message.answer(msg.restart)

@dp.message(Command("feedback"))
async def cmd_start(message: types.Message):
    await message.answer(msg.feedback)

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты сказал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
