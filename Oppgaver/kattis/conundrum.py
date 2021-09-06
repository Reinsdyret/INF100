"""
Now Per has come up with a secret plan: 
every day he will erase one letter of the cipher text and replace it with a different letter, so that, 
in the end, the whole text reads “PerPerPerPerPerPerPer”. Since Per will change one letter each day, 
he hopes that people will not notice.

Per would like to know how many days it will take to transform a given cipher text into a text only containing his name, 
assuming he substitutes one letter each day. You may assume that the length of the original cipher text is a multiple of 3.

For simplicity, you can ignore the case of the letters, and instead assume that all letters are upper-case.
Input

The first and only line of input contains the cipher text on the whiteboard. It consists of at most 300
upper-case characters, and its length is a multiple of 3

.
Output

Output the number of days needed to change the cipher text to a string containing only Per’s name.
"""

cipher = input().lower()

charChange = 0

for p in range(0,len(cipher),3):
    if cipher[p] != "p":
        charChange += 1
        continue

for e in range(1,len(cipher),3):
    if cipher[e] != "e":
        charChange += 1
        continue

for r in range(2,len(cipher),3):
    if cipher[r] != "r":
        charChange += 1
        continue

print(charChange)
