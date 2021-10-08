"""
Write a function that takes in a tuple with three items and change the third item to "salmon"
"""

def swap_tuple(cat:tuple) -> tuple:
    """Takes in a tuple, cat, with three items and change the third item to "salmon"""
    name, personality, food = cat
    food = "salmon"
    return (name,personality, food)
