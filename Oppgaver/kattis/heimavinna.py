"""
Input
The input is one line and specifies the problems that Hneitir needs to solve. Hneitir always need to solve at least one problem. 
The problems are numbered from 1 up to 1000 and are listed in ascending order, separated by semicolons (;). If two or more problems are in a row, that range is specified with -. 
A example of an input is 1-3;5;7;10-13 and this means that Hneitir needs to solve problems 1,2,3,5,7,10,11,12, and 13.

Output
Write out one integer n, the number of problems that Hneitir has to solve."""
import sys

problems = sys.stdin.readline().strip().split(';')
problemCount = 0
i = 0
while i < len(problems):
    for p in range(0,len(problems[i])):
        if problems[i][p] == '-':
            num1 = int(problems[i][:p])
            num2 = int(problems[i][p+1:])
            problemCount += num2 - num1 + 1
            problems.pop(i)
            break
    i += 1

problemCount += len(problems)
print(problemCount)
