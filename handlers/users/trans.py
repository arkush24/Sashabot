from aiogram import types

from googletrans import Translator

from utils.translate.one_world import translate_word
from loader import dp, bot


def translate_word(word: str) -> str:
    if len(word.split()) > 1:
        raise "too many words"

    translator = Translator()
    return translator.translate(word, src='en', dest='ru').text
# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer("Вводи слово я переведу:")
    await message.answer(translate_word(message.text))

