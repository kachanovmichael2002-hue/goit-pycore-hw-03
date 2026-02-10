import re


def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр
    digits = re.sub(r'\D', '', phone_number)

    # Обробка міжнародного коду
    if digits.startswith('380'):
        # Якщо номер починається з 380, додаємо тільки '+'
        normalized = '+' + digits
    elif digits.startswith('0'):
        # Якщо номер починається з 0, додаємо код України '+38'
        normalized = '+38' + digits
    else:
        # В інших випадках просто додаємо '+'
        normalized = '+' + digits

    return normalized


raw_numbers = ["0671234567", "+380501234567", "(050)8889900"]

for number in raw_numbers:
    normalized = normalize_phone(number)
    print(normalized)
