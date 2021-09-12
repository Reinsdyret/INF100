"""
I uke_04_oppg_2.py lag en løkke for å snakke med en dum chatbot, bruk en while True løkke . 
Chatboten kan bare si tre ting: Hei! Vil du snakke med meg?, 
Så kult!, eller Ha det bra! Du må bruke input() for å svare chatboten. 
Bruk break for å avlutte while-løkken når du får inn Nei eller nei.
"""

while True:
    userInput = input("Hei! Vil du snakke med meg? ")
    if (userInput == "Nei") or (userInput == "nei"):
        print("Ha det bra!")
        break
    print("Så kult!")