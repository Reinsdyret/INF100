"""
I filen uke_03_oppg_3.py skal du skrive et program som tar som input først en enhet, enten nanometer ('nm') eller terahertz ('THz'), 
og siden en verdi (et tall). Programmet skal siden skrive ut hvilket spektrum som stråling med den enheten og det verdiet tillhører.

Om du får en verdi som er akkurat på grensen mellom to spektrum så skal du velge den som er overst av de to i listen. 
For eksempel: om brukeren skriver 'nm' og '10' så skal programmet ditt skrive ut at det er ultrafiolett stråling. 
Eller om brukeren skriver 'THz' og '790' så skal programmet ditt skrive ut at det er synlig lys.

Kjøring av programmet ditt skal se ut slik som følgende eksempelkjøringer. Husk at store eller små tall kan også skrives med e-notasjon: 2.5e-4 betyr 2.5·10⁻⁴.
"""

unit = input("Angi enhet: ")
value = float(input("Angi verdi: "))

# Har veldig lyst til å lage to funksjoner, en for nm og en for THz fordi det blir bare mer leselig og mindre iffer inni iffer
# Hvis man skulle gjort dette uten funksjoner ville det bare vært å skrive det inni funksjonene der hvor jeg kaller dem
# Fristet og med et set som lookup for å finne spektrum, men vet ikke hvordan jeg skal få et intervall nøye nok for dette :)
# Også veldig usikker når det kommer til å lage variabler på engelsk eller norsk så beklager hvis det blir litt tullete hvor noen er engelsk og andre norske

def nm(v):
    if v < 0.01:
        return "gammastråling"
    if v >= 0.01 and v < 10:
        return "røntgenstråling"
    if v >= 10 and v < 380:
        return "ultrafiolett stråling"
    if v >= 380 and v < 740:
        return "synlig lys"
    if v >= 740 and v < 10**6:
        return "infrarød stråling"
    if v >= 10**6 and v < 10**9:
        return "mikrobølger"
    if v >= 10**9:
        return "radiobølger"


def thz(v):
    if v <= 3*10**(-4):
        return "radiobølger"
    if v > 3*10**(-4) and v <= 0.3:
        return "mikrobølger"
    if v > 0.3 and v <= 405:
        return "infrarød stråling"
    if v > 405 and v <= 790:
        return "synlig lys"
    if v > 790 and v <= 3*10**4:
        return "ultrafiolett stråling"
    if v > 3*10**4 and v <= 3*10**7:
        return "røntgenstråling"
    if v > 3*10**7:
        return "gammastråling"


if unit == "nm":
    spectrum = nm(value)
else:
    spectrum = thz(value)

print(f"Dette er {spectrum}.")
