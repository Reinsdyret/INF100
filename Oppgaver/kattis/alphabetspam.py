"""
Input

The input consists of:

    one line with a string consisting of at least 1

and at most 100000 characters.

A preprocessing step has already transformed all whitespace characters to underscores (_), 
and the line will consist solely of characters with ASCII codes between 33 and 126 (inclusive).
Output

Output four lines, containing the ratios of whitespace characters, lowercase letters, uppercase letters, 
and symbols (in that order). Your answer should have an absolute or relative error of at most 10−6.
"""

stringInput = input()
charCount = len(stringInput)
whitespaceCharacters = 0
lowercaseLetters = 0
uppercaseLetters = 0
symbols = 0

for character in stringInput:
    if ord(character) > 64 and ord(character) < 91:
        uppercaseLetters += 1
    elif ord(character) > 96 and ord(character) < 123:
        lowercaseLetters += 1
    elif ord(character) == 95:
        whitespaceCharacters += 1
    else:
        symbols += 1
    
print(round(whitespaceCharacters / charCount, 6))
print(round(lowercaseLetters / charCount,6))
print(round(uppercaseLetters / charCount,6))
print(round(symbols / charCount,6))
