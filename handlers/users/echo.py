from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f"Не знаю, что на это ответить...")


    #await bot.send_message(message.from_user.id, f"Не знаю, что на это ответить...")

"""

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
"""
