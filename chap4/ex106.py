# Days in a Month

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


def main():
    month = int(input('enter the month as a number: '))
    year = int(input('enter the year: '))
    if not 1 <= month <= 12:
        print('please enter a valid month')
    else:
        days = days_in_month(month, year)
        print('there are {} in the selected month'.format(days))


if __name__ == '__main__':
    main()
