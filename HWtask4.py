from datetime import datetime, timedelta
from typing import List, Dict


def get_upcoming_birthdays(
    coworkers: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    """
    Формує список колег, у яких день народження
    припадає на найближчі 7 днів від поточної дати.

    Якщо день народження вже минув у поточному році,
    він переноситься на наступний рік.

    Якщо день народження припадає на вихідний
    (суботу або неділю), дата привітання
    переноситься на найближчий понеділок.
    """
    today = datetime.today().date()
    upcoming: List[Dict[str, str]] = []

    for coworker in coworkers:
        birthday = datetime.strptime(
            coworker["birthday"], "%Y-%m-%d"
        ).date()

        birthday_this_year = birthday.replace(year=today.year)

        # якщо вже минув — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": coworker["name"],
                "congratulation_date": congratulation_date.strftime("%Y-%m-%d"),
            })

    return upcoming


def main() -> None:
    """Точка входу в програму."""
    coworkers: List[Dict[str, str]] = [
        {"name": "Іван", "birthday": "1990-02-10"},
        {"name": "Марія", "birthday": "1985-02-15"},
        {"name": "Олег", "birthday": "1992-02-18"},
    ]

    upcoming = get_upcoming_birthdays(coworkers)
    for item in upcoming:
        print(item)


if __name__ == "__main__":
    main()