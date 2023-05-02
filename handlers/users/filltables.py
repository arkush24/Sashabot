from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp, db

from states.reg import RegIn

from utils.parsing.FB_parcer import hendler_top


@dp.message_handler(commands = ['filltables'])
async def bot_reg(message: types.Message):
    hendler_top()
    await message.answer(f"Топы 'Main' обновлены")
