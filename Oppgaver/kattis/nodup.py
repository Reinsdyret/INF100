"""
Input
Input is a line containing words separated by single spaces, where a word consists of one or more uppercase letters. A line contains no more than 80 characters.

Output
The output is "yes" if no word is repeated, and "no" if one or more words repeat."""
import sys

stringList = sys.stdin.readline().split()
stringSet = set(stringList)

if len(stringSet) == len(stringList):
    print("yes")
else:
    print("no")
