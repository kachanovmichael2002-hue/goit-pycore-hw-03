import re
from typing import List


def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону до міжнародного формату.

    Аргументи:
        phone_number (str): номер телефону у довільному форматі.

    Повертає:
        str: номер телефону у форматі +380XXXXXXXXX або подібному.
    """
    # Видаляємо всі символи, крім цифр
    digits: str = re.sub(r"\D", "", phone_number)

    # Обробка міжнародного коду
    if digits.startswith("380"):
        normalized: str = "+" + digits
    elif digits.startswith("0"):
        normalized = "+38" + digits
    else:
        normalized = "+" + digits

    return normalized


def main() -> None:
    """Точка входу в програму."""
    raw_numbers: List[str] = [
        "0671234567",
        "+380501234567",
        "(050)8889900",
    ]

    for number in raw_numbers:
        normalized: str = normalize_phone(number)
        print(normalized)


if __name__ == "__main__":
    main()