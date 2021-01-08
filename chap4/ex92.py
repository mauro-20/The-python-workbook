# Ordinal Date to Gregorian Date

from ex91 import days_in_month, ordinal_date, isLeapYear


# this function will compute the month from an ordinal date
# @param days the days of the ordinal date
# @param year the year of the ordinal date
# @return the correspondent month of the year
def month_calc(days, year):
    days_calc = 0
    for i in range(1, days):
        days_calc += days_in_month(i, year)
        if days_calc >= days:
            return i


# this function will transform an ordinal date to a gregorian date
# @param days the days of the ordinal date
# @param year the year of the ordinal date
# @return a string of the gregorian date dd-mm-yyyy
def ordinal_to_gregorian(days, year):
    # compute the month
    month_date = month_calc(days, year)

    # compute the day of the month
    # sum the days of the previous months
    prev_days_sum = 0
    for i in range(1, month_date):
        prev_days_sum += days_in_month(i, year)
    # subtract the ordinal days to the sum of the days of the previous months
    day_date = days - prev_days_sum

    return day_date, month_date


# this function will receive a date from the user, how many days the user wants to add
# and it will print the date that occurs after those days
def date_sum_days():
    # user inputs
    day_in = int(input('enter the day: '))
    month_in = int(input('enter the month: '))
    year_in = int(input('enter the year: '))
    days_sum = int(input('enter how many days you want to add: '))

    # converting the date in ordinal date for easier calculation
    ordinal_days = ordinal_date(day_in, month_in, year_in)

    # add days to the date
    ordinal_days_sum = ordinal_days + days_sum

    # converting the ordinal date to gregorian date, considering leap years
    if isLeapYear(year_in) and ordinal_days_sum > 366:
        day_out, month_out = ordinal_to_gregorian(ordinal_days_sum - 366, year_in + 1)
        year_out = year_in + 1
    elif not isLeapYear(year_in) and ordinal_days_sum > 365:
        day_out, month_out = ordinal_to_gregorian(ordinal_days_sum-365, year_in+1)
        year_out = year_in + 1
    else:
        day_out, month_out = ordinal_to_gregorian(ordinal_days_sum, year_in)
        year_out = year_in

    # printing the result
    print(f"the due date is {day_out:02}-{month_out:02}-{year_out:04}")


date_sum_days()
