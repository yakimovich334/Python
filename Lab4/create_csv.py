import csv
import random
from faker import Faker
from datetime import datetime

# Ініціалізуємо Faker для генерації даних
fake = Faker('uk_UA')

# Визначаємо кількість записів
num_records = 2000
male_count = int(num_records * 0.6)
female_count = num_records - male_count

# Функція для генерації дати народження
def generate_birth_date():
    start_date = datetime(1938, 1, 1)
    end_date = datetime(2008, 1, 1)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Відкриваємо CSV файл для запису
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    # Генеруємо чоловіків
    for _ in range(male_count):
        writer.writerow({
            'Прізвище': fake.last_name_male(),
            'Ім’я': fake.first_name_male(),
            'По батькові': fake.middle_name_male(),
            'Стать': 'Чоловіча',
            'Дата народження': generate_birth_date().strftime('%d.%m.%Y'),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })
    
    # Генеруємо жінок
    for _ in range(female_count):
        writer.writerow({
            'Прізвище': fake.last_name_female(),
            'Ім’я': fake.first_name_female(),
            'По батькові': fake.middle_name_female(),
            'Стать': 'Жіноча',
            'Дата народження': generate_birth_date().strftime('%d.%m.%Y'),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })

print("CSV файл успішно створений!")
