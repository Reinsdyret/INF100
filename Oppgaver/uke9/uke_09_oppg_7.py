"""Write a function word_comparison() that takes in two strings and returns the common letters
and unique letters for each word in a dictonary"""

def word_comparison(word1,word2:str) -> dict:
    """Takes in two strings and returns the common letters
    and unique letters for each word in a dictonary"""
    the_dictionary = {
            "In common": None,
            "Unique to first word": None,
            "Unique to second word": None,
    }
    # For first word
    common = []
    unique1 = []
    for letter1 in word1:
        if letter1 in word2:
            common.append(letter1)
            continue
        unique1.append(letter1)


    unique2 = []
    for letter1 in word2:
        if letter1 in word1:
            common.append(letter1)
            continue
        unique2.append(letter1)

    the_dictionary["In common"] = set(common)
    the_dictionary["Unique to first word"] = set(unique1)
    the_dictionary["Unique to second word"] = set(unique2)

    return the_dictionary


print(word_comparison("computer","science"))
            
