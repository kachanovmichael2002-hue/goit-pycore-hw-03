import random
def get_numbers_ticket(min_val, max_val, quantity):
    """
    Генерує список унікальних випадкових чисел в заданому діапазоні.

    Аргументи:
        min_val (int): Мінімальне число (не менше 1).
        max_val (int): максимальне число (не більше 1000).
        quantity (int): Ккількість чисел для вибору.

    Повертає:
        list: відсортований список унікальних чисел або порожній список при некоректних параметрах
    """
    # Перевіряємо коректність вхідних параметрів
    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []
    
     # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    return sorted(numbers)
print(get_numbers_ticket(1, 1000, 5))
    