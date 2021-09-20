"""
I denne oppgaven skal vi beregne posisjonen av en sten som droppes fra en høyde. 
I filen uke_04_oppg_11.py skal du lage et program som tar en høyde som input fra brukeren og så printer ut, for hver sekund, 
posisjonen av en sten som droppes fra den høyden, frem til stenen er på marken. Til sist skal programmet printe ut hvor lang tid det tok til stenen landet på marken.

Formelen for stenens posisjon p er følgene
p = p0 - (1/2 gt^2)
"""
# Numpy lib is used to detect sign changes in positions list
import numpy
start_height = float(input("Stenen droppes fra høyde: "))
print(f"Stenen droppes fra høyde: {start_height} m")

# Quick solution for poopyheads that likes to input 0m
if start_height == 0:
    print("Stenen lander mellom -1 og 0 sekunder etter at den droppes.")
    quit()
# Positions list is used to loop over to find what seconds the rock is at 0m
positions = []


def rock_falling(p0,t):
    """Function taking in starting height of object and time object has fallen to return current position of object"""
    g = 9.8
    return p0 - (1/2 * g * t**2)


def zero_crosses(a):
    """Function for finding sign changes in list a, code found on: https://stackoverflow.com/questions/3843017/efficiently-detect-sign-changes-in-python"""
    return numpy.where(numpy.diff(numpy.sign(a)))[0]

current_position = rock_falling(start_height,0)
positions.append(current_position)
for seconds in range(1,6):
    current_position = rock_falling(start_height,seconds)
    positions.append(current_position)
    # The use of max command makes it so that all negative values are forced to be 0 :) found this at https://stackoverflow.com/questions/12518760/how-to-change-a-negative-number-to-zero-in-python-without-using-decision-structu?answertab=votes#tab-top 
    rounded_position = max(round(current_position,1),0)
    if rounded_position == 0:
        print(f"{rounded_position} m")
        break
    print(f"{rounded_position} m")

for zero_cross in zero_crosses(positions):
    print(f"Stenen lander mellom {zero_cross} og {zero_cross+1} sekunder etter at den droppes.")

