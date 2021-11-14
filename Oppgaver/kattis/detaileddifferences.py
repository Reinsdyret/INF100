"""https://open.kattis.com/problems/detaileddifferences"""

def compare_strings(s1,s2:str) -> str:
    compare_result = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            compare_result += "."
            continue
        compare_result += "*"
    return compare_result

n = int(input())
cases = []

for i in range(n):
    string1 = input()
    string2 = input()
    cases.append(tuple((string1,string2)))

for i in range(len(cases)):
    s1,s2 = cases[i]
    print(s1)
    print(s2)
    print(compare_strings(s1,s2))
