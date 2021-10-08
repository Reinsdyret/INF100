def sumThing(p:int) -> int:
    currentSum = 1
    for n in range(p):
        currentSum -= (2**n - 1)/4**n
    return currentSum

print(sumThing(1000000))