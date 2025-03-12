from aiogram import Router, types
from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm import Sta
# from aiohttp.web_routedef import static
#
# from bot.database.crud import delete_user
# from bot.middlewares.restart import delete_user_info

router = Router()

@router.message(Command("restart")) # TODO: /restart (FMS)
async def cmd_restart(message: types.Message):
    pass

# @router.message(Command("restart"), state="*") # TODO: /restart (FMS)
# async def cmd_restart(message: types.Message, state: FSMContext):
    # await state.set_state("waiting for restart conformation")
    # await message.answer("""
# Макс забудет все о вас. Продолждить?
# (Да/Нет)
# """)
#
# @router.message(state="waiting for restart conformation")
# async def conform_restart(message: types.Message, state: FSMContext):
    # conformation_status = message.text.lower().strip()
    # if conformation_status == "да":
        # await delete_user_info()
        # await message.answer("Макс удалил ваш контакт")
        # await state.finish()
    # else:
        # await state.finish()

