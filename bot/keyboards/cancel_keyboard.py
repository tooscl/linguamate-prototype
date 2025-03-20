from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


cancel_button = KeyboardButton(text="Назад")
cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[cancel_button]], resize_keyboard=True)