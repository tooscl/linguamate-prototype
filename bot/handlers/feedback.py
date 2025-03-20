from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.config import ADMIN_ID
from bot.keyboards.cancel_keyboard import cancel_keyboard

router = Router()

class FeedbackForm(StatesGroup): # Создание FSM для формы обратной связи
    waiting_for_feedback = State()


@router.message(Command("feedback"))
async def cmd_feedback(message: types.Message, state: FSMContext):
    await message.answer("Оставьте ваш отзыв о вашем опыте общения с LinguaMate:", reply_markup=cancel_keyboard)
    await state.set_state(FeedbackForm.waiting_for_feedback)

@router.message(FeedbackForm.waiting_for_feedback)
async def receive_feedback(message: types.Message, state: FSMContext):
    if message.text == "Назад":
        await message.answer("Возвращаемся к разговорам!", reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        return

    await message.forward(ADMIN_ID, disable_notification=True)
    await message.answer("Спасибо за ваш отзыв!", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
