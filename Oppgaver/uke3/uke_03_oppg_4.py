"""
Regelen for å beregne om et år er et skuddår eller ikke er som følger:

Vanligvis er et år som er deleligt med 4 et skuddår (for eksempel 1996 var et skuddår).

Men år som også er delelige med 100 (for eksempel 1900) er ikke skuddår.

Unntatt år som er delelige med 400 (for eksempel 2000). Disse er skuddår.

I filen uke_03_oppg_4.py, skriv et program som spør brukeren om et årstall og skriver ut om det er et skuddår eller ikke.
"""

year = int(input("Angi år: "))

# Prøvde litt å få alle if-setningen i en if setning med en kombinasjon av and og or, men slet med logikken

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Dette er et skuddår.")
    elif year % 100 == 0:
        print("Dette er ikke et skuddår.")
    else:
        print("Dette er et skuddår.")
else:
    print("Dette er ikke et skuddår.")
