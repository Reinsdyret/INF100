"""
I uke_04_oppg_5.py skriv en while-løkke som beregner fakulteten (n!) til et heltall fra brukeren. 
For eksempel, 5! = 5 * 4 * 3 * 2 * 1 = 120. Fakulteten til 0 er definert som 1.
"""

factorial = input("Tall: ")
n = int(factorial.replace("_",""))

product = 1
count = 1

while count <= n:
    product *= count
    count += 1

print(product)
