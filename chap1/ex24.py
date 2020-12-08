# Units of Time

min_to_sec = 60
h_to_sec = 60*min_to_sec
day_to_sec = 24*h_to_sec

days = int(input('enter the number of days: '))
hours = int(input('enter the number of hours: '))
minutes = int(input('enter the number of minutes: '))
seconds = int(input('enter the number of seconds: '))

total_seconds = days*day_to_sec + hours*h_to_sec + minutes*min_to_sec + seconds

print('the total of seconds is %d' % total_seconds)
