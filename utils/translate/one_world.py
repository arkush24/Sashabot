from googletrans import Translator
def translate_word(word: str) -> str:
    if len(word.split()) > 1:
        raise "too many words"

    translator = Translator()
    return translator.translate(word, src='en', dest='ru').text