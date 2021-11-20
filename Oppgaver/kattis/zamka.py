"""https://open.kattis.com/problems/zamka"""

def checkSumDigits(num,x):
    num_string = str(num)
    digit_sum = 0
    for i in range(len(num_string)):
        digit_sum += int(num_string[i])

    return digit_sum == x

L = int(input())
D = int(input())
X = int(input())

# Find N
for i in range(L,D+1):
    if checkSumDigits(i,X):
        N = i
        break

# Find M
for i in range(D,L-1,-1):
    if checkSumDigits(i,X):
        M = i
        break

print(N)
print(M)
