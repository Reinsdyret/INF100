"""
Program takes in a valid DNA string and returns it complimentarystring (backwards). 
This means that the bases A,T,C,G are taken in in a series. And the complimentary is A=T and C=G
Make a function that does this:
"""

def complement(dna: str) -> str:
    """Takes in DNA sequense as string and returns the complimentary DNA sequence"""
    returnDna = ""
    complimentary = {
        "A":"T",
        "C":"G",
        "T":"A",
        "G":"C"
    }
    for base in dna:
        returnDna += complimentary[base]

    return returnDna[::-1]
