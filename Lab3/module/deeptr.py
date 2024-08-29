from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def TransLate(text: str, scr: str, dest: str) -> str:
    """Функція повертає текст перекладений на задану мову, або повідомлення про помилку."""
    try:
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначає мову та коефіцієнт довіри для заданого тексту."""
    try:
        detected_lang = detect(text)
        confidence = "Недоступно в цьому модулі"
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return confidence
        elif set == "all":
            return f"Мова: {detected_lang}, Коефіцієнт довіри: {confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"

def CodeLang(lang: str) -> str:
    """Функція повертає код мови або назву мови залежно від введеного параметру."""
    try:
        lang_list = GoogleTranslator().get_supported_languages(as_dict=True)
        if len(lang) == 2:
            return lang_list.get(lang, "Невідомий код мови")
        else:
            for code, name in lang_list.items():
                if name.lower() == lang.lower():
                    return code
            return "Невідома мова"
    except Exception as e:
        return f"Помилка обробки мови: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить таблицю всіх мов, що підтримуються, та їх кодів."""
    try:
        lang_list = GoogleTranslator().get_supported_languages(as_dict=True)
        lines = []
        lines.append(f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text' if text else ''}")
        lines.append("-" * 50)
        
        for i, (code, lang) in enumerate(lang_list.items(), 1):
            translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ''
            lines.append(f"{i:<3} {lang:<20} {code:<10} {translated_text}")
        
        if out == "screen":
            for line in lines:
                print(line)
        elif out == "file":
            with open('languages.txt', 'w', encoding='utf-8') as f:
                f.write("\n".join(lines))
        
        return "Ok"
    except Exception as e:
        return f"Помилка виводу таблиці: {str(e)}"

# Демонстрація роботи функцій
if __name__ == "__main__":
    print(LanguageList("screen", "Добрий день"))
