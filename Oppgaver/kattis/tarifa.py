"""
Input
The first line of input contains the integer X (1≤X≤100). The second line of input contains the integer N (1≤N≤100). Each of the following N lines contains an integer P (0≤P≤10000), the number of megabytes spent in each of the first N months of using the plan. Numbers P will be such that Pero will never use more megabytes than he actually has.

Output
The first and only line of output must contain the required value from the task."""

X = int(input())
N = int(input())
P = []
mbLeft = 0
for i in range(0,N):
    P.append(int(input()))

for i in range(0,N):
    mbLeft += X - P[i]

print(mbLeft + X)