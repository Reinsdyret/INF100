"""
Write a function that takes in a 2d tuple with days and temperatures and returns the same tuple just that the thursday tuple has temperature 12
"""

def adjust_daily_temps(week:tuple) -> tuple:
    """Takes in a 2d tuple with days and temperatures and returns the same tuple just that the thursday tuple has temperature 12"""
    monday, tuesday, wednesday, thursday, friday, saturday = week
    day, temp = thursday
    temp = 12.0
    thursday = (day,temp)
    return (monday, tuesday, wednesday, thursday, friday, saturday)
