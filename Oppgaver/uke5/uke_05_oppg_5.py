"""
I denne oppgaven skal vi lage våre egne funksjoner som beregner maximum, minimum og absoluttverdi av to tall. 
Vi skal også beregne lengden til en streng.

Vi skal sammenligne disse med Pythons innebygde funksjoner max(), min(), abs() og len().
"""
import math


def egen_abs(a):
    """Function takes in integer a and returns the absolute value of a"""
    if a < 0:
        a *= -1
    return a


def egen_max(a,b):
    """Function takes in integers a and b, then returns the highest value of those"""
    return int(((a+b)+egen_abs(a-b))/2)


def egen_min(a,b):
    """Function takes in integers a and b, then returns the lowest value of those"""
    return int(((a+b)-egen_abs(a-b))/2)


def egen_len(text):
    """Function takes in string and returns length of string, letter 必 while not be counted if its in the string"""
    #text += "必"
    #char = ""
    #counter = 0
    #while char != "必":
    #    char = text[counter]
    #    counter += 1
    #return counter - 1
    # Thought the above solution was cool, but realized quick that the easier would be the following
    counter = 0
    for char in text:
        counter += 1
    return counter
