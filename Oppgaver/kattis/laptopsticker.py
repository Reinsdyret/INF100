"""https://open.kattis.com/problems/laptopsticker"""

widthC, heightC, widthS, heightS = map(int,input().split(" "))

sticker_possible = widthC >= widthS + 2 and heightC >= heightS + 2

output = 1 if sticker_possible else 0

print(output)
