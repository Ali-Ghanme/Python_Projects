import datetime
import os
import time

now = datetime.datetime.now()

# Choose 6PM today as the time the alarm fires.
# This won't work well if it's after 6PM, though.
alarm_time = datetime.datetime.combine(now.date(), datetime.time(18, 0, 0))

# Think of time.sleep() as having the operating system set an alarm for you,
# and waking you up when the alarm fires.
time.sleep((alarm_time - now).total_seconds())

os.system(r"D:\Programming Project\Python Project\music.mp3")