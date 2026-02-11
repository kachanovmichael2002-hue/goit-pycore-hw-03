from datetime import datetime


def get_days_from_today(date_str: str) -> int:
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
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError(
            "Невірний формат дати. Використовуйте 'YYYY-MM-DD'."
        ) from exc

    today = datetime.today().date()
    delta = today - given_date

    return delta.days


def main() -> None:
    """Точка входу в програму."""
    result: int = get_days_from_today("2027-02-01")
    print(result)


if __name__ == "__main__":
    main()