"""
Use the datetime library to find how many wednesdays there were
from 1. januar 1901 to 31 desember 2000."""
import datetime

def iter_days(year):
    """A generator with all dates in a year"""
    dt = datetime.date(year, 1, 1)
    while dt.year == year:
        yield dt
        dt += datetime.timedelta(days=1)

wednesday_count = 0
for year2 in range(1901,2001):
    for date in iter_days(year2):
        if date.weekday() == 2 and date.day == 1:
            wednesday_count += 1

print(wednesday_count)
