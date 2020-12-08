# Current Time

import time

local_time = time.localtime()
t = time.asctime(local_time)

print('the local time is', t)