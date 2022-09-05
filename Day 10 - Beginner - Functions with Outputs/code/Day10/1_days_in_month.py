# TODO Convert this function is_leap() so that instead of printing "Leap year." or "Not leap year."
#  it should return True if it is a leap year and return False if it is not a leap year.
def is_leap(year_input):
    """Checks if the year informed in the parameter is a leap year and returns a boolean for that."""
    if year_input % 4 == 0:
        if year_input % 100 == 0:
            if year_input % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO You are then going to create a function called days_in_month() which will take a year and a month as inputs
#   and it will use this information to work out the number of days in the month, then return that as the output
#   The List month_days contains the number of days in a month from January to December for a non-leap year.
#   A leap year has 29 days in February.
def days_in_month(year_input, month_input):
    """Returns the number of days in a month, in a specific year informed by parameters """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_input) and month_input == 2:
        return month_days[month_input - 1] + 1
    else:
        return month_days[month_input - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

