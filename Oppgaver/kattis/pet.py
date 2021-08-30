"""
In the popular show “Dinner for Five”, five contestants compete in preparing culinary delights. 
Every evening one of them makes dinner and each of other four then grades it on a scale from 1 to 5. 
The number of points a contestant gets is equal to the sum of grades they got. The winner of the show is of course the contestant that gets the most points.

Write a program that determines the winner and how many points they got.

Input
Five lines, each containing 4 integers, the grades a contestant got. The contestants are numbered 1 to 5 in the order in which their grades were given.

Output
Output on a single line the winner’s number and their points, separated by a space. The input data will guarantee that the solution is unique."""
import sys

ratings = []
ratingSums = []

for i in range(0,5):
    ratings.append(sys.stdin.readline().split())

for i in range(0,5):
    groupSum = 0
    for p in range(0,len(ratings[i])):
        groupSum += int(ratings[i][p])
    ratingSums.append(groupSum)

maxValue = max(ratingSums)
print(ratingSums.index(maxValue) + 1, maxValue)
