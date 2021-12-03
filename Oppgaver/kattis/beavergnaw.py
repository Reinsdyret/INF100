"""https://open.kattis.com/problems/beavergnaw"""
import math

def calculate_d(D:int,V:int) -> float:
    

treeD, volume = map(int,input().split())

while volume != 0 and treeD != 0:
    print(calculate_d(treeD,volume))
    treeD, volume = map(int,input().split())
