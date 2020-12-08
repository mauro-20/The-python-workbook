# Units of Time (Again)

sec_to_min = 1/60
sec_to_h = sec_to_min/60
sec_to_day = sec_to_h/24
min_to_sec = 60
h_to_sec = 60*min_to_sec
day_to_sec = 24*h_to_sec

seconds_input = int(input('enter seconds: '))

days = seconds_input//day_to_sec
rem = seconds_input % day_to_sec
hours = rem//h_to_sec
rem = rem % h_to_sec
minutes = rem//min_to_sec
seconds = rem % min_to_sec

print('the equivalent time is %d:%02d:%02d:%02d' %(days, hours, minutes, seconds))
