"""
Input

The input is composed of two lines. The first line contains a single positive integer n
(1≤n≤100) that specifies the number of temperatures collected by the University of Chicago Weather Service. 
The second line contains n temperatures, each separated by a single space. 
Each temperature is represented by an integer t (−1000000≤t≤1000000)
Output

You must print a single integer: the number of temperatures strictly less than zero.
"""
input()

temperatures = input().strip().split()
count = 0

for i in range(len(temperatures)):
    if int(temperatures[i]) < 0:
        count += 1

print(count)
