"""Write several functions for handling the file VIK_sealevel_2000
containing sealevel data (year month day hour):
1. read_file(filename) takes in a filename and opens it and returns a list of tuples with 5 items

2. average(data, month=None) that takes in the list of tuples and month with a default value of None
the function should give the average height of the month given,
if month is None the average of all heights should be returned.

3. add_weekday(data) takes in the list of tuples and returns a new list of tuples but with 6 items.
The last item in the tuple is the day. 1. Jan 2000 was a saturday and 31. dec 2000 was a sunday.

4. average_weekday(data, weekday) takes in the list of tuples with six items and returns the
average of said weekday.
"""
#import os.path

def read_file(filename:str) -> list:
    """Takes in a filename and opens it and returns a list of tuples with data from file"""
    file_data = []
    # with open(os.path.dirname(__file__) + "/" + filename,"r",encoding="utf-8") as sealeveldata:
    with open(filename, "r", encoding="utf-8") as sealeveldata:
        for line in sealeveldata:
            year, month, day, hour, height = line.strip().split(" ")
            file_data.append(tuple((int(year),int(month),int(day),int(hour),int(height))))

    return file_data


def average_all_months(data:list) -> float:
    """Takes in a list of tuples and returns the average of the last item in the tuples"""
    sum_heights = 0
    count = 0
    for year, data_month, day, hour, height in data:
        sum_heights += height
        count += 1

    return sum_heights/count


def average(data:list, month=None) -> float:
    """Takes in the list of tuples and month with a default value of None
    the function should give the average height of the month given,
    if month is None the average of all heights should be returned."""
    if month is None:
        return average_all_months(data)
    sum_heights = 0
    count = 0

    for year, data_month, day, hour, height in data:
        if data_month == month:
            sum_heights += height
            count += 1
    return sum_heights / count


def add_weekday(data:list) -> list:
    """Add weekdays as a last item for the tuples in the list. First day is saturday"""
    new_data_list = []
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    current_day = 4 # It will start on saturday but it starts at 4 cause for loop will add 1
    last_day = 0

    for year, month, day, hour, height in data:
        if last_day != day:
            current_day += 1
        if current_day > 6:
            current_day = 0
        new_data_list.append(tuple((year,month,day,hour,height,days[current_day])))

        last_day = day

    return new_data_list


def average_weekday(data:list, weekday:str) -> float:
    """Takes in list of data and weekday and returns the average of the data to that weekday"""
    sum_heights = 0
    count = 0

    for year, month, day, hour, height, day_str in data:
        if day_str == weekday:
            sum_heights += height
            count += 1

    return sum_heights/count
