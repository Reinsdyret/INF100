"""https://open.kattis.com/problems/batterup"""

N = int(input())
bats = map(int,input().split(" "))

sum_positive_bats = 0
for bat in bats:
    if bat < 0: N += bat
    else: sum_positive_bats += bat

print(sum_positive_bats / N)
