"""
In this contest, you also earn a carrot for each difficult problem you solve, or huffle-puff problems as we prefer to call them.
You will be given the number of contestants in a hypothetical contest, the number of huffle-puff problems that people solved in the contest and a description of each contestant. 
Now, find the number of carrots that will be handed out during the contest.

Input
Input starts with two integers 1≤N,P≤1000 on a single line, denoting the number of contestants in the contest and the number of huffle-puff problems solved in total. 
Then follow N lines, each consisting of a single non-empty line in which the contestant describes him or herself. 
You may assume that the contestants are good at describing themselves, in a way such that an arbitrary 5-year-old with hearing problems could understand it.

Output
Output should consist of a single integer: the number of carrots that will be handed out during the contest."""

a, b = input().split()
a = int(a)
b = int(b)
for i in range(0,a):
    input()

print(b)