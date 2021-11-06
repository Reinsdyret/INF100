"""First line of input if N that specifies how many lines of input follows
The next N lines contain one word and every other word starting at the first shall be printed out"""

N = int(input())
inputs = []

for i in range(0,N):
    inputs.append(input())

for i in range(len(inputs)):
    if i % 2 == 0:
        print(inputs[i])
