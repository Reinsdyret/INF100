"""https://open.kattis.com/problems/zanzibar"""

def calculate_immigrant_turtle(turtle_history:list) -> int:
    total_immigrants = 0
    for i in range(0,len(turtle_history) -1):
        if int(turtle_history[i]) < int(turtle_history[i+1])/2:
            total_immigrants += int(turtle_history[i+1]) /2 - int(turtle_history[i])
    
    return int(total_immigrants * 2)

n = int(input())

cases = []

for i in range(n):
    case = input().split(" ")
    cases.append(case[:-1])


for i in range(len(cases)):
    print(calculate_immigrant_turtle(cases[i]))
