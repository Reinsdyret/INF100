"""https://open.kattis.com/problems/shatteredcake"""

cake_width = int(input())
pieces = int(input())

total_areal = 0

for i in range(pieces):
    piece_width, piece_length = map(int,input().split(" "))
    total_areal += piece_width * piece_length

print(int(total_areal / cake_width))
