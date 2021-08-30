"""
Input
Standard input consists of several transcripts. Each transcript consists of a number of paired guesses and responses. 
A guess is a line containing single integer between 1 and 10 (inclusive), and a response is a line containing “too high”, “too low”, or “right on”. 
Each game ends with “right on”. A line containing 0 follows the last transcript. There are at most 2500 guess-response pairs in total.

Output
For each game, output a line “Stan is dishonest” if Stan’s responses are inconsistent with the final guess and response. Otherwise, print “Stan may be honest”."""
import sys

numbers = []
responses = []

a = ''
i = 2
while a != '0':
    if i % 2 == 0:
        line = sys.stdin.readline().strip()
        numbers.append(line)
        a = line
    else:
        a = sys.stdin.readline().strip().split()
        responses.append(a[1])
    i += 1
print(numbers,responses)
