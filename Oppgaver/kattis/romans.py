"""https://open.kattis.com/problems/romans"""
import math

def normal_round(n):
    """https://stackoverflow.com/a/41206290"""
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def roman_paces(miles:float) -> int:
    not_rounded = miles * (5280000/4854)
    return normal_round(not_rounded)

english_miles = float(input())

print(roman_paces(english_miles))
