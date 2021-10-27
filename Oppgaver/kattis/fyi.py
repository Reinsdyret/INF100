"""Take phone number as input and output 1 if three first digits are 5 else 0"""

phone_number = input()

output = 1 if phone_number[0] == "5" and phone_number[1] == "5" and phone_number[2] == "5" else 0

print(output)