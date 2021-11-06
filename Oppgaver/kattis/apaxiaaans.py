"""https://open.kattis.com/problems/apaxiaaans"""

name = input()

last_letter = ""
compact_name = ""

for letter in name:
    if letter != last_letter:
        compact_name += letter
    last_letter = letter

print(compact_name)
