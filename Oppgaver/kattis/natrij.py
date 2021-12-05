"""https://open.kattis.com/problems/natrij
NOT WORKING"""
from datetime import datetime, timedelta

time1 = input()
time2 = input()

FMT = "%H:%M:%S"

delta_time = datetime.strptime(time2, FMT) - datetime.strptime(time1,FMT)

if delta_time.days < 0:
    delta_time = timedelta(
        days = 0,
        seconds=delta_time.seconds,
        microseconds=delta_time.microseconds
    )

delta_time = "0" + str(delta_time)

print(delta_time)
