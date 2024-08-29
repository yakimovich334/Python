from langdetect import detect, DetectorFactory
from langdetect import detect_langs
from googletrans import Translator
import pycountry

# Ініціалізація генератора для детектора
DetectorFactory.seed = 0

def LangDetect(text):
    try:
        detected = detect_langs(text)[0]  # Отримуємо першу мову з найвищою ймовірністю
        lang_code = detected.lang
        confidence = detected.prob
        return f"Detected(lang={lang_code}, confidence={confidence})"
    except Exception as e:
        return f"Error: {str(e)}"

def TransLate(text, lang):
    translator = Translator()

    # Спроба отримати код мови з назви або ISO-коду
    try:
        if len(lang) > 2:
            lang_code = pycountry.languages.get(name=lang.capitalize()).alpha_2
        else:
            lang_code = lang
    except AttributeError:
        return "Error: Language not recognized."
    
    # Переклад тексту
    try:
        translated = translator.translate(text, dest=lang_code)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang):
    try:
        if len(lang) == 2:  # Якщо введено ISO-код
            lang_name = pycountry.languages.get(alpha_2=lang).name
        else:  # Якщо введено назву мови
            lang_name = lang.capitalize()
        return lang_name
    except AttributeError:
        return "Error: Language code not recognized."

# Приклад використання
txt = "Доброго дня. Як справи?"
lang = "en"
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))
