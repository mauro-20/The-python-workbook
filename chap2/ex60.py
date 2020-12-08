# What Day of theWeek Is January 1?

import math

year = int(input('enter a year: '))

jan_1 = (year + math.floor((year-1)/4)-math.floor((year-1)/100)+math.floor((year-1)/400)) % 7

if jan_1 == 0:
    day = 'Sunday'
elif jan_1 == 1:
    day = 'Monday'
elif jan_1 == 2:
    day = 'Tuesday'
elif jan_1 == 3:
    day = 'Wednesday'
elif jan_1 == 4:
    day = 'Thursday'
elif jan_1 == 5:
    day = 'Friday'
elif jan_1 == 6:
    day = 'Saturday'

print('January 1st in %d is %s' % (year, day))
