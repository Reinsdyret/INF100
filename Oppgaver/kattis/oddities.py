"""https://open.kattis.com/problems/oddities"""

def even(num:int) -> bool:
    if num % 2 == 0:
        return True
    return False

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for number in numbers:
    status = "even" if even(number) else "odd"
    print(f"{number} is {status}")
