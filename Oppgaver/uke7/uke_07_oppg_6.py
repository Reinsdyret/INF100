"""
Write a function pigify() that takes a one word string and returns the pigified version
Write a function pigify_sentence() that takes in a sentence as string and returns the sentenced where each word is pigified
"""

def pigify(word:str) -> str:
    """Takes in a one word in string and returns the pigified version"""
    vowels = ["a","e","i","o","u"]
    if word[0] in vowels:
        return word + "way"
    
    lettersBeforeVowel = ""
    for index, letter in enumerate(word):
        if letter in vowels:
            return word[index:] + lettersBeforeVowel + "ay"
        lettersBeforeVowel += letter

    return word + "ay"


def pigify_sentence(sentence:str) -> str:
    """Takes in a sentence as string and returns the sentenced where each word is pigified"""
    wordList = sentence.split(" ")
    pigifiedWordList = []
    for word in wordList:
        pigifiedWordList.append(pigify(word))
    return " ".join(pigifiedWordList)
