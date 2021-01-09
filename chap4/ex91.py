# Gregorian Date to Ordinal Date


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# define days in a month
def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def ordinal_date(day, month, year):
    # day input control
    if day > days_in_month(month, year):
        raise ValueError('invalid day')
    # month input control
    if month > 12 or month < 1:
        raise ValueError('invalid month')
    # compute the ordinal date
    ordinal_days = 0
    for i in range(1, month):
        ordinal_days += days_in_month(i, year)
    ordinal_days += day
    return ordinal_days


def main():
    day = int(input('enter the day: '))
    month = int(input('enter the month: '))
    year = int(input('enter the year: '))
    print(f"the corresponding ordinal date is {ordinal_date(day, month, year)}")


if __name__ == '__main__':
    main()