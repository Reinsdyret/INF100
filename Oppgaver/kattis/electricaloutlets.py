"""Recieve first input is how many lines input following
the next n lines describe some power oulets ans tuff"""

N = int(input())

sum_power_stuff = 0

for i in range(N):
    inputs = list(map(int,input().split(" ")))
    for inp in inputs:
        sum_power_stuff += inp
    print(sum_power_stuff - len(inputs) - 1)
    sum_power_stuff = 0

