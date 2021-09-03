"""
Find number of combinations of input
input is one line with integers separated by a space
"""

import sys

nums = sys.stdin.readline().split()
product = 1

for i in range(len(nums)):
    product *= int(nums[i])

sys.stdout.write(str(product))