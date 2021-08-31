'''
I denne oppgaven skal vi spørre brukeren om en haiku og siden printe den på en fin måte på skjermen.

I filen uke_02_oppg_6.py, skriv kode som gjør følgende, i oppgitt rekkefølge:

Spør brukeren om første raden i en haiku.

Spør brukeren om andre raden i en haiku

Spør brueren om tredje raden i en haiku.

Printer en tom linje

Printer hele haikuen med høyrejustering og med en ramme av «@» runt (se eksempelkjøring).

(Tips: bruk len() og max() til å finne lengden av den lengste raden. 
Siden printer du hver rad med så mange mellomrom før raden som det er forskjell mellom den raden og den lengste raden i haikun. 
Husk å printe en rad med «@» før og etter haikuen og husk å printe «@» i starten og slutten av hver rad med tekst. 
Hvor mange tegn lengre må toppen og bunnen av rammen være enn den lengste raden i haikuen?)
'''


firstLine = input('Første raden: ')
secondLine = input('Andre raden: ')
thirdLine = input('Tredje raden: ')
lines = [firstLine, secondLine, thirdLine]

longest = lines[0]
for i in range(1,len(lines)):
    if len(longest) > len(lines[i]):
        continue
    longest = lines[i]

# + 4 so because of 1 space on either side of line, plus the needed '@' to connect walls
print('\n' + '@' * (len(longest) + 4))
for i in range(0,len(lines)):
    spaces = ' ' * (len(longest) - len(lines[i]))
    print('@' + ' ' + spaces + lines[i] + ' ' +  '@')

print('@' * (len(longest) + 4))
