from aiogram import Router, types
from aiogram.filters import Command

from bot.keyboards.hello_keyboard import hello_keyboard

router = Router()

@router.message(Command("start")) # TODO: FSM регистрации
async def cmd_start(message: types.Message):
    await message.answer("""
Привет! Добро пожаловать в LinguaMate! 🚀 

LinguaMate — это ваш персональный AI-напарник для практики иностранных языков. Он поможет вам погрузиться в языковую среду, даже если вокруг никто не говорит на нужном языке.  

🗣 Говорите естественно — чат-бот поддерживает живые диалоги и адаптируется к вашему стилю общения.  
💡 Учитесь легко — получайте обратную связь, улучшайте произношение и расширяйте словарный запас.  
🎭 В будущем — выбор персонажей! Пока что в прототипе доступен только Макс — ваш британский друг по переписке со школьных времен. Но впереди вас ждёт больше собеседников!  

👀 Готовы попробовать? Просто напишите "Hello Max!"
❓ Нужна помощь? Введите /help.
""", reply_markup=hello_keyboard)