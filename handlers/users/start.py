from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.translate.one_world import translate_word
import os.path
from loader import dp, bot
from datetime import datetime
from keyboards.inline import choise_buttons

#from utils.parsing.FB_parcer import saw_names
name = ''
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    sti = open('other/stickers/hello.webp', 'rb')

    await message.answer_sticker(sti)
    await message.answer(f"Привет, будущий англичанин, {message.from_user.full_name}!\nЯ - <b>Помошник в изучении английского языка</b>, бот созданный, что бы помочь тебе.",parse_mode='html', reply_markup=choise_buttons.choise)
    name = (f"{message.from_user.full_name}")

@dp.callback_query_handler(text_contains="my_w")
async def buying_pear(call: CallbackQuery):
    #await call.answer(cache_time=60)
    await call.bot.send_message(call.from_user.id, "Вот все слова которые ты запомнил")

    def get_all_user_words(user: str) -> list:
        full_filename = 'us_names/' + user
        if not os.path.exists(full_filename):
            raise 'no words for this user'

        words = []
        with open(full_filename, 'r') as f:
            words = [line.rstrip() for line in f]

        return words
    print(str(get_all_user_words(call.from_user.full_name)))
    await call.bot.send_message(call.from_user.id, "\n".join(get_all_user_words(call.from_user.full_name)))


@dp.callback_query_handler(text_contains="data")
async def buying_pear(call: CallbackQuery):
    await call.bot.send_message(call.from_user.id, "Вот дата сегодняшнего дня")
    def get_current_date() -> str:
        return f"{datetime.now().strftime('%Y')}-{datetime.now().strftime('%B')}-{datetime.now().day} ({datetime.now().strftime('%A')})"

    await call.bot.send_message(call.from_user.id, get_current_date())

@dp.callback_query_handler(text_contains="help")
async def buying_pear(call: CallbackQuery):
    text = ("Список команд: ",
            "/translate - Перевести слово(недоделано)",
            "/start - поздроваться(начать)")

    await call.bot.send_message(call.from_user.id, "\n".join(text))