"""
Vanligvis sier mann at et menneskeår er ekvivalent med 7 hundeår. Dette tar dokk ikke hensyn til at hunder blir voksne på ca 2 år. 
Derfor kan det være bedre å regne begge de første 2 menneskeårene som 10.5 hundeår, og etter det regne hvert menneskeår som 4 hundeår.

I filen uke_03_oppg_5.py skal du skrive et program som spør brukeren om antall menneskeår og siden skriver ut hvor mange hundeår det tilsvarer.
"""

humanYears = int(input("Angi menneskeår: "))


if humanYears > 2:
    dogYears = (2 * 10.5) + (humanYears - 2) * 4
else:
    dogYears = humanYears * 10.5

print(f"Dette tilsvarer {dogYears} hundeår.")
