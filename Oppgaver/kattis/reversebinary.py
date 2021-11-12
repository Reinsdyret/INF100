"""https://open.kattis.com/problems/reversebinary"""

number = int(input())

binary_number = bin(number)[2:]

print(int(binary_number[::-1],2))
