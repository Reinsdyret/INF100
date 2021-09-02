"""
The factorial of N, written as N!, is defined as the product of all the integers from 1 to N. For example, 3!=1×2×3=6.

This number can be very large, so instead of computing the entire product, just compute the last digit of N! (when N! is written in base 10).

Input
The first line of input contains a positive integer 1≤T≤10, the number of test cases. Each of the next T lines contains a single positive integer N. N is at most 10.

Output
For each value of N, print the last digit of N!.
"""
import sys

t = int(input())
n = []
factorialLastDigits = [1,1,2,6,4,0,0,0,0,0,0]
answers = ""
for i in range(t):
    n.append(int(input()))

for i in range(len(n)):
    sys.stdout.write(str(factorialLastDigits[n[i]]) + "\n")
