"""https://open.kattis.com/problems/autori"""

name = input()

short_name = ""

for i in range(len(name)):
    if name[i-1] == "-" or i == 0:
        short_name += name[i]

print(short_name)
