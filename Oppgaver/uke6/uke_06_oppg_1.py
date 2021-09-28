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
    maxLen = 8 if len(theList) >= 8 else len(theList)
    for i in range(0,maxLen,2):
        newList.append(theList[i])

    return newList

def reverse(theList):
    return theList[::-1]

def double_values(theList):
    yList = []
    for element in theList:
        yList.append(element*2)
    
    return yList

def unique_values(theList):
    return list(dict.fromkeys(theList))

print(every_other([1, 2, 3, 4, 3]))