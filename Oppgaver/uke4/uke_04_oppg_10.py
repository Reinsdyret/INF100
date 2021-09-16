"""
I denne oppgaven skal vi beregne temperaturen av 250.0 mL vann som varmes opp fra romtemperatur (25.0°C) 
til kokepunktet (100.0°C).

For enkelhets skyld, anta at temperaturen til vannet øker lineært med 0.625 C/s

I filen uke_04_oppg_10.py skal du lage et programm som begynner med temperaturen 25.0°C 
og så printer ut for hver sekund temperaturen til vannet frem til det kokes på 100.0°C.

Til slutt skal programmet printe ut hvor lang tid det tok å nå kokepunktet med frasen 100.0°C i {resultat her} sekunder.

Vis resultatet til nærmeste tiende, men bruk full presision i beregningen. 
(Om du ser 26.2°C etter 2s har du brukt de avrundete verdiene)
"""
#Importer decimal biblioteket for decimalhåndtering slik som ble sagt i en forelesning, gjelder bare for 26.3 avrunding
# from decimal import Decimal, ROUND_HALF_UP

temperature = 25.0
speed = 0.625
seconds = 0

while temperature < 100:
    # Avrunde løsning funnet fra https://gist.github.com/jackiekazil/6201722 FOR Å RUNDE 26.25 OPP TIL 26.3
    #rounded = Decimal(temperature.quantize(Decimal('.1'), rounding=ROUND_HALF_UP))
    rounded = round(temperature,1)

    print(f"{seconds}s = {rounded}°C")
    temperature += speed
    seconds += 1

print(f"100.0°C i {seconds} sekunder")