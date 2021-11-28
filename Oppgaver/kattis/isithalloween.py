"""https://open.kattis.com/problems/isithalloween"""

halloween = ["OCT","31"]

halloween2 = ["DEC","25"]

date_to_be = input().split()

if date_to_be == halloween or date_to_be == halloween2:
    print("yup")
else:
    print("nope")
