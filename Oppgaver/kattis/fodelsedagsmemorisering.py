"""https://open.kattis.com/problems/fodelsedagsmemorisering"""
from operator import itemgetter

n = int(input())

birthdays = []

none_colliding_birthdays = []

for i in range(n):
    name, rating, day_month = input().split()
    day, month = day_month.split("/")
    date_rating = int(day)/int(month)
    birthdays.append([name,int(rating),date_rating])

sorted_birthdays_by_rating = sorted(birthdays,key=itemgetter(1))

dates_used = []

birthdays.reverse()

for i in range(len(birthdays)):
    for p in range(i+1,len(birthdays)):
        if birthdays[i][2] != birthdays[p][2] and birthdays[i][2] in dates_used:
            continue
        if birthdays[i][2] in dates_used:
            continue
        else:
            none_colliding_birthdays.append(birthdays[i])
            if birthdays[i][2] == birthdays[p][2]:
                dates_used.append(birthdays[i][2])

sorted_birthdays_by_date = sorted(none_colliding_birthdays,key=itemgetter(2))

print(len(sorted_birthdays_by_date))

names = []
for name, rating, date in sorted_birthdays_by_date:
    names.append(name)
    print(name)
