"""https://open.kattis.com/problems/datum"""
import datetime

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day, month = map(int,input().split(" "))

dt = datetime.datetime(2009,month,day)

print(days[dt.weekday()])
