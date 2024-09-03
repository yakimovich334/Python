import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

try:
    # Зчитування CSV файлу
    df = pd.read_csv('D:\LabPython\Python\Lab4\employees.csv', encoding='utf-8')
    print("Ok")
except FileNotFoundError:
    print("Помилка: CSV файл не знайдено.")
    exit()

# Додавання стовпця "Вік"
df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d.%m.%Y')
df['Вік'] = df['Дата народження'].apply(lambda x: datetime.now().year - x.year - ((datetime.now().month, datetime.now().day) < (x.month, x.day)))

# Кількість чоловіків та жінок
gender_counts = df['Стать'].value_counts()
print("Кількість співробітників за статтю:")
print(gender_counts)

# Діаграма для статі
gender_counts.plot(kind='bar', title='Кількість співробітників за статтю')
plt.show()

# Кількість співробітників за віковими категоріями
age_categories = {
    'younger_18': df[df['Вік'] < 18],
    '18-45': df[(df['Вік'] >= 18) & (df['Вік'] <= 45)],
    '45-70': df[(df['Вік'] > 45) & (df['Вік'] <= 70)],
    'older_70': df[df['Вік'] > 70]
}

print("Кількість співробітників за віковими категоріями:")
for category, data in age_categories.items():
    print(f"{category}: {len(data)}")
    data['Стать'].value_counts().plot(kind='bar', title=f'Кількість співробітників за статтю в категорії {category}')
    plt.show()

# Кількість співробітників за статтю у вікових категоріях
for category, data in age_categories.items():
    gender_category_counts = data['Стать'].value_counts()
    print(f"Кількість співробітників за статтю в категорії {category}:")
    print(gender_category_counts)
    gender_category_counts.plot(kind='bar', title=f'Кількість співробітників за статтю в категорії {category}')
    plt.show()
