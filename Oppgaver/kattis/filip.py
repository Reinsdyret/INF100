"""Take in two 3 digit numbers and return the highest but if the numbers were reversed"""

num_a, num_b = map(int,input().split(" "))

num_a = int(str(num_a)[::-1])
num_b = int(str(num_b)[::-1])

max_num = max(num_a, num_b)

print(max_num)