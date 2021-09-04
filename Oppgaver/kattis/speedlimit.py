"""
Input

The input consists of one or more data sets (at most 10). 
Each set starts with a line containing an integer n, 1≤n≤10, followed by n pairs of values, one pair per line. 
The first value in a pair, s, is the speed in miles per hour and the second value, t, is the total elapsed time. 
Both s and t are integers, 1≤s≤90 and 1≤t≤12. The values for t are always in strictly increasing order. A value of −1 for n
signals the end of the input.

Output

For each input set, print the distance driven, followed by a space, followed by the word “miles”.
"""
import sys

n = 0

output = []
miles = []
hours = []

n = sys.stdin.readline().strip()

while n != "-1":
    tempMiles = []
    tempHours = []
    for i in range(int(n)):
        d, t = sys.stdin.readline().strip().split()
        tempMiles.append(int(d))
        tempHours.append(int(t))
    miles.append(tempMiles)
    hours.append(tempHours)
    n = sys.stdin.readline().strip()

for i in range(len(hours)):
        for p in range(len(hours[i]) - 1, 0, -1):
            hours[i][p] -= hours[i][p-1]


for i in range(len(hours)):
    output.append(sum([a*b for a,b in zip(hours[i],miles[i])]))

for i in range(len(output)):
    sys.stdout.write(str(output[i]) + " miles" + "\n")
