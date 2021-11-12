"""https://open.kattis.com/problems/modulo"""

numbers = []

for i in range(10):
    numbers.append(int(input()) % 42)

print(len(set(numbers)))
