from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp, db

from states.reg import RegIn

@dp.message_handler(commands = ['registrate'])
async def bot_reg(message: types.Message):
    await message.answer(f"Заглушка ненужной регистрации:")



'''
пока не надо

@dp.message_handler(commands = ['registrate'])
async def bot_reg(message: types.Message):
    await message.answer(f"Введите Логин:")
    await RegIn.nickname.set()

@dp.message_handler(state=RegIn.nickname)
async def answer_nickname(message:types.Message, state: FSMContext):
    answer1 = message.text

    await state.update_data( name = answer1)

    await message.answer(f"Введите Пароль:")
    await RegIn.password.set()

@dp.message_handler(state=RegIn.password)
async def answer_password(message:types.Message, state: FSMContext):
    answer2 = message.text
    await state.update_data(passw = answer2)
    data = await state.get_data()
    await state.reset_state(with_data=False)

    if(not db.users_exists(message.from_user.id)):
        #если юзера нет то, добавляем его
        db.add_users(message.from_user.id, data.get("name"),data.get("passw"))
        await message.answer(f"Вы успешно зарегистрированы!")
    else:
        await message.answer(f"Вы уже зареганы")
'''
