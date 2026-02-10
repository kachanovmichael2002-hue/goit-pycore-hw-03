from datetime import datetime


def get_days_from_today(date_str) -> int:
    """
    Обчислює кількість днів між сьогоднішньою датою
    та заданою датою.

    Аргументи:
        date_str (str): дата у форматі 'YYYY-MM-DD'.

    Повертає:
        int: кількість днів.
             Додатне число — якщо дата у минулому,
             від’ємне — якщо дата у майбутньому.
    """
    try:
        # Перетворюємо рядок у об'єкт дати без часу
        given_date = datetime.strptime(
            date_str, "%Y-%m-%d"
        ).date()
    except ValueError:
        # Якщо формат неправильний — повідомляємо користувача
        raise ValueError(
            "Невірний формат дати. Використовуйте 'YYYY-MM-DD'."
        )

    today = datetime.today().date()
    delta = today - given_date

    return delta.days


print(get_days_from_today("2027-02-01"))