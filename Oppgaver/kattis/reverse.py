"""
Input
The first line of input contains the integer n. Then comes a list of n integers, each on its own line.

Output
The list should be printed in reverse order of input.
"""

def reverse(list):
    arr = []
    for i in range(len(list) - 1, -1, -1):
        arr.append(list[i])
    return arr


n = int(input())
startList = []
for i in range(0,n):
    startList.append(int(input()))

reversedList = reverse(startList)
for i in range(0,len(reversedList)):
    print(reversedList[i])
