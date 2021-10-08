"""
Write to functions, 
update_weather() which takes in string of space seperated floats and returns tuple of all the floats
tuesday_weather() which takes in a tuple of floats and returns the second float
"""

def update_weather(temperatures: str) -> tuple:
    """Takes in string of space seperated floats and returns tuple of all the floats"""
    return tuple(map(float,temperatures.split(" ")))
    

def tuesday_weather(temperatures:tuple) -> float:
    """Takes in a tuple of floats and returns the second float"""
    return list(temperatures)[1]