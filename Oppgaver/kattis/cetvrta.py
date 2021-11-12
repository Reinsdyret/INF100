"""https://open.kattis.com/problems/cetvrta"""

xs = []
ys = []

for i in range(3):
    x, y = map(int,input().split(" "))
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

final_x = xs[2] if xs[0] == xs[1] else xs[0]
final_y = ys[2] if ys[0] == ys[1] else ys[0]

print(f"{final_x} {final_y}")
