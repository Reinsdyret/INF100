"""
I filen uke_02_oppg_3.py, skriv kode som gjør følgende, i oppgitt rekkefølge:

Spør brukeren om en vekt i enheten stones og enheten pounds via to input() funksjoner, og lagre inputen i to variabler.

Beregner tilsvarende vekt til summen av inputvektene, i enheten kilogram. Konverter først stones til kilogram med formelen
V(kg) = (V(st)/0.15747)
 
hvor V(kg) er vekten i kilogram og V(st) er vekten i stones. Konverter siden pounds til kilogram med formelen

V(kg) = V(lb) / 2.20462
hvor V(kg) er vekten i kilogram og V(lb) er vekten i pounds. Summér til sist de to verdiene du har beregnet.

Print resultatet.
"""

stone = int(input("Vekt i stones: "))
pound = int(input("Vekt i pounds: "))

kiloStone = stone / 0.15747
kiloPound = pound / 2.20462

print("Vekt i kilogram: ", kiloStone + kiloPound)
