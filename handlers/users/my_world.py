from aiogram import types

from googletrans import Translator

from utils.translate.one_world import translate_word
from loader import dp, bot



def save_word_to_file(user: str, word: str):
    full_filename = 'users/' + user
    if not os.path.exists(full_filename):
        with open(full_filename, 'w'):
            pass

    with open(full_filename, 'a+') as f:
        f.write(word + '\n')