"""Write a function first_letter_last_word(filename) that loops over lines in file and
returns a string of all the first letters in the last word per line"""
# Used for getting path of file
#import os.path

def first_letter_last_word(filename:str) -> str:
    """Takes in text file and returns a string of all the first letters in the last word per line"""
    letters = ""
    # Os.path stuff just says the path of this file
    # with open(os.path.dirname(__file__) + "/" + filename,"r", encoding="utf-8") as readfile:
    with open(filename,"r",encoding="utf-8") as readfile:
        for line in readfile:
            words = line.strip("\n").split(" ")
            last_word = words[len(words) -1]
            letters += last_word[0]
    return letters
