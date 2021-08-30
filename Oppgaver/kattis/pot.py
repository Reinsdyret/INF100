"""
For example, without text formatting, the original task in the form of X=212+1253 became a task in the form of X=212+1253. 
Help the teacher by writing a program that will, for given N integers from P1 to PN determine and output the value of X from the original task.

Input
The first line of input contains the integer N (1≤N≤10), the number of the addends from the task. 
Each of the following N lines contains the integer Pi (10≤Pi≤9999, i=1,…,N) from the task.

Output
The first and only line of output must contain the value of X (X≤1000000000) from the original task."""
import sys

n = sys.stdin.readline().strip()
numbers = []
sum = 0
for i in range(0,int(n)):
    numbers.append(sys.stdin.readline().strip())

for i in range(0,len(numbers)):
    sum += int(numbers[i][:-1]) ** int(numbers[i][-1])

print(sum)
