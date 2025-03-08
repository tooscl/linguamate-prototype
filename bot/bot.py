import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import requests

from config import TOKEN

import messages as msg

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

API_URL = "http://localhost:8000"
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
# Работа с LLM
@dp.message()
async def handle_text(message: types.Message):
    response = requests.post(f"{API_URL}/message", json={"user_id": message.from_user.id, "text": message.text})
    await message.answer(response.json()["response"])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
