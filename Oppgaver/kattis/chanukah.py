"""https://open.kattis.com/problems/chanukah"""

def chanukah(days:int) -> int:
    """takes in integer and returns the sum of integers up to and including days
    Adds days to the total aswell"""
    candles = days
    for i in range(1,days+1):
        candles += i
    return candles

N = int(input())

cases = []

for i in range(N):
    k, d = map(int,input().split(" "))
    cases.append(chanukah(d))

for i in range(len(cases)):
    print(f"{i+1} {cases[i]}")
