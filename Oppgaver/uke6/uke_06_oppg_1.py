"""
Make following functions for lists: remove_sevens(), every_other(), reverse(), double_values(), unique_values()
all taking a list of numbers in as parameters and returning a new list based on the function
"""

def remove_sevens(theList:list) -> list:
    while True:
        try:
            theList.remove(7)
        except:
            return theList

def every_other(theList:list) -> list:
    newList = []
    maxLen = 8 if len(theList) >= 8 else len(theList)
    for i in range(0,maxLen,2):
        newList.append(theList[i])

    return newList

def reverse(theList:list) -> list:
    return theList[::-1]

def double_values(theList: list) -> list:
    yList = []
    for element in theList:
        yList.append(element*2)
    
    return yList

def unique_values(theList:list) -> list:
    return list(dict.fromkeys(theList))