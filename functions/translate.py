from googletrans import Translator

def translate_text(txt):
    translator = Translator()
    result = translator.translate(txt, dest='ru')
    return result.text