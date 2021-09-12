"""
I uke_04_oppg_6.py bruk while-løkker for å skrive ut dette mønsteret (for hver rad øker/minsker vi med 2 mellomrom):

Eksempelkjøring:
*
  *
    *
      *
        *
      *
    *
  *
*
"""

row = 0
spaces = -2

while row < 5:
    spaces += 2
    print(spaces * " " + "*")
    
    row += 1

while row < 9:
    spaces -= 2
    print(spaces * " " + "*")
    row += 1
