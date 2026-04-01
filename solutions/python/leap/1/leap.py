def leap_year(year):
    """Checks if year is leap year
    :param year: int - The year to check
    :return: bool - True if year is a leap year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
