"""
Input

The input contains one line, which has two integers a
and b, separated by a single space. The bounds on these values are 0≤a,b≤1000000

.
Output

Output the sum of the two integers, a+b.
"""
import sys

a, b = sys.stdin.readline().strip().split()

sys.stdout.write(str(int(a) + int(b)))