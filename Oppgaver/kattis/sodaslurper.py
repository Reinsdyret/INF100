"""https://open.kattis.com/problems/sodaslurper"""
import math

def slurpSoda(e,f,c:int) -> int:
    drunken = 0
    sum_e_f = e + f

    while sum_e_f >= c:
        sum_e_f = sum_e_f - c + 1
        drunken += 1
    
    return drunken

e, f, c = map(int,input().split(" "))

print(slurpSoda(e,f,c))
