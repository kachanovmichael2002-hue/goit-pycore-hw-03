import random
from typing import List


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> List[int]:
    """
    Генерує список унікальних випадкових чисел у заданому діапазоні.

    Аргументи:
        min_val (int): мінімальне число (не менше 1).
        max_val (int): максимальне число (не більше 1000).
        quantity (int): кількість чисел для вибору.

    Повертає:
        List[int]: відсортований список унікальних чисел
                   або порожній список при некоректних параметрах.
    """

    # Перевірка коректності вхідних параметрів
    if (
        min_val < 1
        or max_val > 1000
        or min_val > max_val
        or quantity < 1
        or quantity > (max_val - min_val + 1)
    ):
        return []

    # Генерація унікальних випадкових чисел
    numbers: List[int] = random.sample(
        range(min_val, max_val + 1),
        quantity
    )

    return sorted(numbers)


def main() -> None:
    """Точка входу в програму."""
    ticket: List[int] = get_numbers_ticket(1, 1000, 5)
    print(ticket)


if __name__ == "__main__":
    main()