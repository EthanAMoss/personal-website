from datetime import date


def calculate_age(birthday):
    """Calculates the current age (in years) of the person with the given birthday"""
    today = date.today()
    age = today.year - birthday.year

    # If today's date is before birthdate, then subtract a year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age = age - 1

    return age