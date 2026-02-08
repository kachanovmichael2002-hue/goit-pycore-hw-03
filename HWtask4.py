from datetime import datetime, timedelta
def get_upcoming_birthdays(coworkers):
    today = datetime.today().date() # Поточна дата
    upcoming = []  # Список для результату
    for coworker in coworkers:
        birthday = datetime.strptime(coworker['birthday'], "%Y-%m-%d").date() # Дата народження колеги
        birthday_this_year = birthday.replace(year=today.year)
        # Якщо день народження вже минув у цьому році, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            days_until_birthday = (birthday_this_year - today).days
            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5:  # Субота
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:  # Неділя
                    congratulation_date += timedelta(days=1)
                upcoming.append({
    "name": coworker["name"],
    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
})
                return upcoming