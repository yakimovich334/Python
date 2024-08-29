from googletrans import Translator
from googletrans import LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Функція повертає текст перекладений на задану мову, або повідомлення про помилку."""
    try:
        translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначає мову та коефіцієнт довіри для заданого тексту."""
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        elif set == "all":
            return f"Мова: {detected.lang}, Коефіцієнт довіри: {detected.confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"

def CodeLang(lang: str) -> str:
    """Функція повертає код мови або назву мови залежно від введеного параметру."""
    try:
        if len(lang) == 2:
            return LANGUAGES.get(lang, "Невідомий код мови")
        else:
            for code, name in LANGUAGES.items():
                if name.lower() == lang.lower():
                    return code
            return "Невідома мова"
    except Exception as e:
        return f"Помилка обробки мови: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить таблицю всіх мов, що підтримуються, та їх кодів."""
    try:
        lines = []
        lines.append(f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text' if text else ''}")
        lines.append("-" * 50)
        
        for i, (code, lang) in enumerate(LANGUAGES.items(), 1):
            translated_text = translator.translate(text, dest=code).text if text else ''
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
