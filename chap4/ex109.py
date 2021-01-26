# Magic Dates

from ex106 import days_in_month


# Determine whether or not a date is "magic"
# @param day the day portion of the date
# @param month the month portion of the date
# @param year the year portion of the date
# @return True if the date is magic, False otherwise
def is_magic_date(day, month, year):
    year_digit = str(year)[-2:]
    if day * month == int(year_digit):
        return True
    else:
        return False


# Find and display all of the magic dates in the 1900s
def main():
    for year in range(1900, 2000):
        for month in range(1, 12+1):
            for day in range(1, days_in_month(month, year)+1):
                if is_magic_date(day, month, year):
                    print('{}/{}/{}'.format(day, month, year))


if __name__ == '__main__':
    main()
