from datetime import datetime, timedelta


def get_upcoming_birthdays(coworkers):
    """
    Формує список колег, у яких день народження
    припадає на найближчі 7 днів від поточної дати.

    Якщо день народження вже минув у поточному році,
    він переноситься на наступний рік.

    Якщо день народження припадає на вихідний
    (суботу або неділю), дата привітання
    переноситься на найближчий понеділок.

    Параметри:
        coworkers (list): список словників, де кожен словник містить:
            - "name": ім'я колеги
            - "birthday": дату народження у форматі YYYY-MM-DD

    Повертає:
        list: список словників з ключами:
            - "name": ім'я колеги
            - "congratulation_date": дата привітання у форматі YYYY-MM-DD
    """
    today = datetime.today().date()
    upcoming = []

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
                "congratulation_date": congratulation_date.strftime("%Y-%m-%d")
            })

    return upcoming