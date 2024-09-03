import pandas as pd
from datetime import datetime

try:
    # Зчитування CSV файлу
    df = pd.read_csv('D:\LabPython\Python\Lab4\employees.csv', encoding='utf-8')
except FileNotFoundError:
    print("Помилка: CSV файл не знайдено.")
    exit()

# Додавання стовпця "Вік"
df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d.%m.%Y')
df['Вік'] = df['Дата народження'].apply(lambda x: datetime.now().year - x.year - ((datetime.now().month, datetime.now().day) < (x.month, x.day)))

# Створення категорій
younger_18 = df[df['Вік'] < 18]
age_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
age_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
older_70 = df[df['Вік'] > 70]

# Запис у XLSX файл
try:
    with pd.ExcelWriter('employees.xlsx') as writer:
        df.to_excel(writer, sheet_name='all', index=False)
        younger_18.to_excel(writer, sheet_name='younger_18', index=False)
        age_18_45.to_excel(writer, sheet_name='18-45', index=False)
        age_45_70.to_excel(writer, sheet_name='45-70', index=False)
        older_70.to_excel(writer, sheet_name='older_70', index=False)
    print("Ok")
except Exception as e:
    print(f"Помилка при створенні XLSX файлу: {e}")
