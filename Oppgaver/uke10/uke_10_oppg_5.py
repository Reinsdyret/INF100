"""Do the same as in last task but this time you dont know if the file exists or not
Return an empty string if there is an error opening the file
Make a function first_letters(filename) that checks and uses the function from oppg_4"""
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


def first_letters(filename:str) -> str:
    """Test if file exist and run first_letter_last_word if so, else return empty string"""
    try:
        return first_letter_last_word(filename)
    except FileNotFoundError:
        return ""
