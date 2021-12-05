"""
Input
The input is one line and specifies the problems that Hneitir needs to solve. Hneitir always need to solve at least one problem. 
The problems are numbered from 1 up to 1000 and are listed in ascending order, separated by semicolons (;). If two or more problems are in a row, that range is specified with -. 
A example of an input is 1-3;5;7;10-13 and this means that Hneitir needs to solve problems 1,2,3,5,7,10,11,12, and 13.

Output
Write out one integer n, the number of problems that Hneitir has to solve."""

problems = input().split(";")
sum_problems = 0

for problem in problems:
    if "-" in problem:
        num1, num2 = map(int,problem.split("-"))
        sum_problems += num2 - num1 + 1
    else:
        sum_problems += 1

print(sum_problems)
