"""
Input
The input contains one line, which has two integers a and b, separated by a single space. The bounds on these values are 0≤a,b≤1000000.

Output
Output the smaller number first, and the larger number second."""

nums = input().split()
output = []
if int(nums[0]) < int(nums[1]):
    output.append(nums[0])
    output.append(nums[1])
else:
    output.append(nums[1])
    output.append(nums[0])
print(output[0], output[1])
