"""
Task

Write a program to compute the most likely outcomes for the sum of two dice rolls. 
Assume each die has numbered faces starting at 1 and that each face has equal roll probability.
Input

The input consists of a single line with two integer numbers, N,M, specifying the number of faces of the two dice.
Constraints

4≤N,M≤20

Number of faces.
Output

A line with the most likely outcome for the sum; in case of several outcomes with the same probability, 
they must be listed from lowest to highest value in separate lines.
"""
import sys

N, M = sys.stdin.readline().strip().split()

numbers = [0] * (int(N) + int(M))
outcomes = []
output = []


for i in range(1,int(N) + 1):
    for p in range(1,int(M) + 1):
        outcomes.append(i+p)


for i in range(len(outcomes) - 1):
    numbers[outcomes[i]] += 1

for i in range(len(numbers)):
    for p in range(i,len(numbers)):
        if numbers[i] < numbers[p]:
            numbers[i] = 0
        elif numbers[p] < numbers[i]:
            numbers[p] = 0

for i in range(len(numbers)):
    if numbers[i] > 0:
        print(i)

