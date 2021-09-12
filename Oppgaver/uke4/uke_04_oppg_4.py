"""
I uke_04_oppg_4.py skriv en for-løkke eller while-løkke som sjekker alle tallene fra 12 til 27 
og skriver ut «{x} er et partall!» hvis partall og «{x} er et oddetall!» hvis oddetall.
"""

for i in range(12,28):
    if i % 2 == 0:
        print(f"{i} er et partall!")
    else:
        print(f"{i} er et oddetall!")
