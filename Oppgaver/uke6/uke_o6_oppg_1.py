"""
Make following functions for lists: remove_sevens(), every_other(), reverse(), double_values(), unique_values()
all taking a list of numbers in as parameters and returning a new list based on the function
"""

def remove_sevens(theList):
    while True:
        try:
            theList.remove(7)
        except:
            return theList

def every_other(theList):
    newList = []
    for i in range(0,8,2):
        newList.append(theList[i])

    return newList

def reverse(theList):
    return theList[::-1]

def double_values(theList):
    for element in theList:
        element *= 2
    
    return theList

def unique_values(theList):
    return list(set(theList))