"""https://open.kattis.com/problems/trik"""

def swapA(ball_pos:int) -> int:
    if ball_pos == 1:
        ball_pos = 2
    elif ball_pos == 2:
        ball_pos = 1
    return ball_pos

def swapB(ball_pos:int) -> int:
    if ball_pos == 3:
        ball_pos = 2
    elif ball_pos == 2:
        ball_pos = 3
    return ball_pos

def swapC(ball_pos:int) -> int:
    if ball_pos == 3:
        ball_pos = 1
    elif ball_pos == 1:
        ball_pos = 3
    return ball_pos

moves = input()

ball_position = 1
functions = {
    "A":swapA,
    "B":swapB,
    "C":swapC
}

for move in moves:
    ball_position = functions[move](ball_position)

print(ball_position)
