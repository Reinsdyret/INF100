"""Recieve first input is how many lines input following
the next n lines are cases
the first input on the line is how many power strips in this case and the following are holes"""

N = int(input())

sum_power_stuff = 0

for i in range(N):
    inputs = list(map(int,input().split(" ")))
    for i in range(1,len(inputs) - 1):
        sum_power_stuff += inputs[i] - 1
    print(sum_power_stuff + inputs[len(inputs) -1])
    sum_power_stuff = 0

