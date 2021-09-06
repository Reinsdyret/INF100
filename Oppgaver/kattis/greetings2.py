"""
Given a string of the form he…ey of length at most 1000, print the greeting you will respond with, containing twice as many e’s.
Input
    The input consists of one line containing a single string s as specified, of length at least 3 and at most 1000

    .

Output
Output the required response.

"""

message = input()

print("h" + ("e" * ((len(message) -2) * 2)) + "y")
