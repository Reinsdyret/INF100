'''
I filen uke_02_oppg_5.py, skriv kode som gjør følgende, i oppgitt rekkefølge:

Leser inn brukerens navn via input().

Leser inn brukerens gateadresse via input().

Leser inn brukerens postkode og poststed via input().

Printer hvor lang den lengste raden er.
'''


svar1 = input('Hva er ditt navn? ')
svar2 = input('Hva er din adresse? ')
svar3 = input('Hva er ditt postnummer og poststed?  ')

svar = [svar1,svar2,svar3]

lengst = svar[0]
for i in range(1,len(svar)):
    if len(lengst) > len(svar[i]):
        continue
    lengst = svar[i]

print(len(lengst))
