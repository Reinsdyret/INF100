"""
You are playing the following simple game with a friend:

The first player picks a positive integer X.

The second player gives a list of k positive integers Y1,…,Yk such that (Y1+1)(Y2+1)⋯(Yk+1)=X, and gets k points.

Write a program that plays the second player.

Input
The input consists of a single integer X satisfying 103≤X≤109, giving the number picked by the first player.

Output
Write a single integer k, giving the number of points obtained by the second player, assuming she plays as good as possible.
"""
import math

X = int(input())
factors = []
divisor = 2

def isPrime(n):
    """NOT MY CODE
    CODE FROM: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/ """
 
    if(n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                return True
            else:
                return False
    else:
        return False

if(isPrime(X)):
    print("1")
    exit()

while X > 1:
    if X % divisor != 0:
        divisor += 1
        continue
    
    factors.append(divisor)
    X = X / divisor
    divisor = 2
        
    if divisor > X ==  0:
        break
print(len(factors))
