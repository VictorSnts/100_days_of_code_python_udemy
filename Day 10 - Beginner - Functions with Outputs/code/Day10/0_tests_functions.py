# TODO Docstrings
def is_leap(year):
    """Checks if the year informed in the parameter is a leap year and returns a boolean for that."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

