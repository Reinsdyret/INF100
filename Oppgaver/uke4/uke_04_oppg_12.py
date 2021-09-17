"""
I filen uke_04_oppg_12.py skal du skrive et program som spør brukeren om et binært tall og siden skriver ut hvilket heltall det er (i basen 10).
"""

binary_number = input("Binært tall: ")
decimal_number = 0

digit_counter = len(binary_number) - 1
for digit_place in range(len(binary_number)):
    decimal_number += int(binary_number[digit_place]) * (2 ** digit_counter)
    digit_counter -= 1

print(decimal_number)