"""
Her skal vi gjøre nesten samme sak igjen, men med en liten forskjell. 
I filen uke_03_oppg_2.py skal du skrive et program som leser inn navn, gateadresse, postkode og poststed fra brukeren og siden skriver ut den/de lengste radene. 
Så denne gang om flere rader har den lengste lengden skal programmet skrive ut alle disse radene.
"""
# Skriver akkurat likt som oppgave 1 med små unntak
navn = input('Hva er ditt navn? ')
adresse = input('Hva er din adresse? ')
post = input('Hva er ditt postnummer og poststed? ')

lengste = []

# Kopi fra forrige oppgave for å finne i hvertfall en lengste
longest_length = navn
if len(navn) < len(adresse):
    longest_length = adresse
elif len(navn) < len(post):
    longest_length = post

if len(adresse) < len(post):
    longest_length = post

lengste.append(longest_length)

# Finner alternativt andre like lange
if len(lengste[0]) == len(navn) and lengste[0] != navn:
    lengste.append(navn)
if len(lengste[0]) == len(adresse) and lengste[0] != adresse:
    lengste.append(adresse)
if len(lengste[0]) == len(post) and lengste[0] != post:
    lengste.append(post)

for i in lengste:
    print(i)
