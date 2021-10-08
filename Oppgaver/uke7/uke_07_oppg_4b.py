"""
Write a function, data_reorganize(), that takes in 2d tuple where the innter tuples have two items. 
And return a 2d tuple where the tuples are the items splitted. Example: data_reorganize((
    ("helo", 2),
    ("Dont", 3)
))
becomes:
(
    ("helo", "Dont"),
    (2,3)
)
"""

def data_reorganize(week:tuple) -> tuple:
    """Takes in 2d tuple where the innter tuples have two items. And return a 2d tuple where the tuples are the items splitted."""
    listWeek = list(week)
    days = []
    temps = []
    for day, temp in listWeek:
        days.append(day)
        temps.append(temp)
    return (tuple(days),tuple(temps))
