from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("""
Привет! Это прототип LinguaMate. 

Что такое Linguamate?
LinguaMate — это решение на основе искусственного интеллекта для людей, которые хотят погрузиться в языковую среду, которую они выбрали, даже находясь вдали от неё. 

Это друг в вашей телефонной книге, который всегда рад поболтать о вашем или ЕГО дне.

Здесь вы можете пообщатся с Максом, вашим другом по переписке из Британии еще со школьных деньков!

/help - для помощи
""")