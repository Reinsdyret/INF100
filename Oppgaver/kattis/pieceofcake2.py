"""https://open.kattis.com/problems/pieceofcake2"""

cake_side, cut_down, cut_right = map(int,input().split(" "))

side1 = cut_down if cut_down > cake_side/2 else cake_side - cut_down
side2 = cut_right if cut_right > cake_side/2 else cake_side-cut_right

print(side1 * side2 * 4)
