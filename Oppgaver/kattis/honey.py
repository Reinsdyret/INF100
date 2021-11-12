"""https://open.kattis.com/problems/honey"""

def create_list(n:int) -> list:
    the_list = [6]
    for i in range(int(n/2-1)):
        the_list.append(the_list[-1] * 15)
    return the_list
cases = int(input())
walks = create_list(14)

for case in range(cases):
    number = int(input())
    print(walks[int(number/2 - 1)])
