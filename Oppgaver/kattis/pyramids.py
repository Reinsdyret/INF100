"""https://open.kattis.com/problems/pyramids"""

def pyramid(n:int)->int:
    """Get the blocks of a pyramid with n height"""
    blocks = 0

    for i in range(0,n,):
        blocks += (i * 2 + 1) ** 2
    return blocks

input_blocks = int(input())

pyramids = [pyramid(i) for i in range(500)]

for i in range(0,len(pyramids)):
    if pyramids[i] > input_blocks:
        print(i-1)
        break
