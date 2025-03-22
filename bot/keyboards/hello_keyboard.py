from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


hello_button = KeyboardButton(text="Hello Max!")
hello_keyboard = ReplyKeyboardMarkup(keyboard=[[hello_button]], resize_keyboard=True, one_time_keyboard=True)