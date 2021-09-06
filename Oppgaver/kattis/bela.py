"""
Write a programme that will determine and output the number of points in the game.
Input

The first line contains the number of hands N
(1≤N≤100) and the value of suit B (S, H, D, C) from the task. 
Each of the following 4N lines contains the description of a card (the first character is the number of the i

-th card (A, K, Q, J, T, 9, 8, 7), and the second is the suit (S, H, D, C)).
Output

The first and only line of output must contain the number of points from the task.
"""
import sys

notDominant = {
    "A" : 11,
    "K" : 4,
    "Q" : 3,
    "J" : 2,
    "T" : 10,
    "9" : 0,
    "8" : 0,
    "7" : 0
}

dominant = {
    "A" : 11,
    "K" : 4,
    "Q" : 3,
    "J" : 20,
    "T" : 10,
    "9" : 14,
    "8" : 0,
    "7" : 0
}

N, domSuit = input().strip().split()

hands = []
points = 0

for i in range(4 * int(N)):
    hands.append(sys.stdin.readline().strip())

for hand in hands:
    if hand[1] == domSuit:
        points += dominant[hand[0]]
        continue
    points += notDominant[hand[0]]

print(points)
