"""https://open.kattis.com/problems/ladder"""

# Using formula D = H / sin(a)
import math

height, angle = map(int, input().split(" "))

print(math.ceil(height / (math.sin(math.radians(angle)))))
