from datetime import datetime

def get_days_from_today(date_str) -> int:
    """
    Обчислює кількість днів від сьогоднішньої дати до заданої дати.

    Аргументи:
        date_str (str): Дата у форматі 'YYYY-MM-DD'

    Повертає:
        int: Кількість днів. Додатнє число, якщо дата у минулому,
             від’ємне — якщо дата у майбутньому.
    """
    try: 
        # Перетворюємо рядок у об'єкт дати без часу
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        # Якщо формат неправильний — повідомляємо користувачу
        raise ValueError("Невірний формат дати. Використовуйте 'YYYY-MM-DD'.")
    
    # Отримуємо поточну дату без часу
    today = datetime.today().date()
    # Різниця між сьогоднішньою датою і заданою датою
    delta = today - given_date 
    # Повертаємо кількість днів (може бути від'ємним, якщо дата в майбутньому)
    return delta.days

print(get_days_from_today("2027-02-01"))