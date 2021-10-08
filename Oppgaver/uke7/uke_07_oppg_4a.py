"""
Write a function, tuple_repack(), that takes in two tuples of "cat info" and returns a list of the two second items in the tuples
"""

def tuple_repack(cat1, cat2 : tuple) -> list:
    """Takes in two tuples of "cat info" and returns a list of the two second items in the tuples"""
    return list(list(zip(cat1,cat2))[1])
