"""https://open.kattis.com/problems/sibice"""
import math

matches, width, length = map(int,input().split(" "))

results = []

hypothenus = math.sqrt(width ** 2 + length ** 2)

for i in range(matches):
    match_length = int(input())
    result = "NE" if match_length > hypothenus else "DA"
    results.append(result)

for result in results:
    print(result)
