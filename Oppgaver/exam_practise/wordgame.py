import random
import time

start_time = time.time()

words = ["bjarte", "kantina", "lars", "vridd","penis"]
word = list(words[random.randint(0,4)])

solved = False
solved_count = 0

unsolved_characters = list(len(word) * "*")
guessed = 1

while True:
    if time.time() - start_time > 30:
        print(f"Du klarte {solved_count} ord på 30 sekunder")
        break
    output_unsolved = "".join(unsolved_characters)
    if word == unsolved_characters:
        print(f"Riktig ordet er {output_unsolved}")
        solved = True

    if guessed == 7:
        print("Du kan ikke gjette mer! GGWP")
        solved = True

    if solved:
        solved_count += 1
        keep_going = input("Fortsette?: (ja/nei)")
        if keep_going == "nei":
            print(f"Du løste {solved_count} ord!")
            break
        word = list(words[random.randint(0,4)])
        unsolved_characters = list(len(word) * "*")
        output_unsolved = "".join(unsolved_characters)
        guessed = 1
        solved = False

    
    print(f"Ordet er {output_unsolved}")
    guess = input(f"Bokstav eller løsning ({guessed}/6): ")

    word_str = "".join(word)

    if word_str == guess:
        print("Riktig!")
        solved = True
        
    for i in range(len(word)):
        if word[i] == guess:
            unsolved_characters[i] = guess

    guessed += 1
