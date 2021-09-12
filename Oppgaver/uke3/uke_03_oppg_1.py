"""
Vi skal utøke programmet fra oppgave 5 førrige uken. 
I filen uke_03_oppg_1.py skal du skrive et program som leser inn navn, gateadresse, postkode og poststed fra brukeren og siden skriver ut den lengste raden i adressen. 
Om flere rader har den lengste lengden skal programmet bare skrive ut den første av de radene som har lengst lengde.
"""

navn = input('Hva er ditt navn? ')
adresse = input('Hva er din adresse? ')
post = input('Hva er ditt postnummer og poststed? ')

# Vet at dette er en treig bubble sort type ting men ville bruke det vi har lært
longest_length = navn
if len(navn) < len(adresse):
    longest_length = adresse
elif len(navn) < len(post):
    longest_length = post

if len(adresse) < len(post):
    longest_length = post

print(longest_length)
