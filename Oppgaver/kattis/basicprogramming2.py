"""
Input
The first line of the input contains an integer N
and t (3≤N≤200000; 1≤t≤5).
The second line of the input contains N non-negative 32-bit signed integers.

Output
For each test case, output the required answer based on the value of t"""
from os import dup
import sys


inp = list(map(int,sys.stdin.readline().strip().split()))
n = inp[0]
t = inp[1]
nums = list(map(int,sys.stdin.readline().strip().split()))


def func1(l):
    output = "No"
    for i in range(0,len(l)):
        for p in range(i,len(l)):
            if l[i] == l[p]:
                continue
            if l[i] + l[p] == 7777:
                output = "Yes"
    
    return output


def func2(l):
    setL = set(l)
    output = "Unique"
    if len(setL) != len(l):
        output = "Contains duplicate"
    return output


def func3(l):
    # Test that there even is a repeating number in the list
    testSet = set(l)
    tester = len(l) - len(testSet) > n/2
    if (tester == False):
        return -1
    dupCount = 0
    output = -1
    for i in range(0,len(l)):
        for p in range(i,len(l)):
            if l[i] == l[p]:
                dupCount += 1
                continue
            break
        if dupCount > n/2:
            output = l[i]
            break
        dupCount = 0
    return output


def func4(l):
    l.sort()
    output = 0
    if n % 2 != 0:
        print("odd")
        return l[int(n/2)]
    output = [l[int(n/2 - 0.5)], l[int(n/2 + 0.5)]]
    return str(output[0]) + " " + str(output[1])


def func5(l):
    newList = [item for item in l if item <= 999 and item >= 100]
    newList.sort()
    for i in range(0,len(newList)):
        newList[i] = str(newList[i])
    return " ".join(newList)


functions = [func1,func2,func3,func4,func5]
print(functions[t-1](nums))
