import string

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # Зчитуємо весь текст
            text = file.read()
            # Розбиваємо текст на речення
            sentences = text.split('.')
            # Знаходимо перше речення і виводимо його
            first_sentence = sentences[0].strip()
            print(f"Перше речення: {first_sentence}")
            
            # Видаляємо пунктуацію з тексту
            translator = str.maketrans('', '', string.punctuation)
            clean_first_sentence = first_sentence.translate(translator)
            # Розбиваємо перше речення на слова
            words = clean_first_sentence.split()

            # Сортуємо українські та англійські слова окремо
            ukr_words = sorted([word for word in words if all('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)])
            eng_words = sorted([word for word in words if all('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in word)])

            # Виводимо українські слова
            if ukr_words:
                print("Українські слова в алфавітному порядку:")
                for word in ukr_words:
                    print(word)
            
            # Виводимо англійські слова
            if eng_words:
                print("Англійські слова в алфавітному порядку:")
                for word in eng_words:
                    print(word)

            # Виводимо загальну кількість слів у першому реченні
            print(f"Кількість слів у першому реченні: {len(words)}")

    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")

# Виклик функції
file_name = 'D:\\LabPython\\Python\\Lab5\\text.txt'
read_file(file_name)
