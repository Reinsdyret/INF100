"""Take in N that says how many numbers to sum from next line"""
N = input()

numbers = input().split()

sum = 0

for integer in numbers:
    sum += int(integer)
print(sum)
