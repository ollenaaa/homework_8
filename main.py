"""
main.py: This script contains a function for getting birthdays per week.
"""
from datetime import date, datetime


def get_birthdays_per_week(users_list):
    """
        Gets a dictionary containing the users' birthdays.

        :return: A dictionary where the keys are the days of the week,
        and the values are the names of birthday people.
    """
    need_to_celebrate = {}
    current_datetime = date.today()

    for user in users_list:
        updated_datetime = user['birthday'].replace(year=datetime.now().year)

        if current_datetime.isocalendar()[1] == updated_datetime.isocalendar()[1] and \
                current_datetime.isocalendar()[2] <= updated_datetime.isocalendar()[2]:

            if updated_datetime.isocalendar()[2] >= 6:
                need_to_celebrate.setdefault('Monday', []).append(user['name'])
            else:
                weekday = updated_datetime.strftime('%A')
                need_to_celebrate.setdefault(weekday, []).append(user['name'])

        elif current_datetime.isocalendar()[1] + 1 == updated_datetime.isocalendar()[1] and \
                current_datetime.isocalendar()[2] > updated_datetime.isocalendar()[2]:
            weekday = updated_datetime.strftime('%A')
            need_to_celebrate.setdefault(weekday, []).append(user['name'])

    return need_to_celebrate


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
