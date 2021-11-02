"""Write two functions:
kast_n_2(n) takes in int n and simulates throwing two dice n times
returns a list of the sum of the n throws

print_histo(xs) that takes in a list and prints a histogram of the occuring integers
for our dice list it would be how many times a sum between 2 and 12 occurs
the histogram consists of * where one * is 1%"""
import random
import collections

def kast_n_2(n:int) -> list:
    n_throws = []
    for _ in range(0,n):
        n_throws.append(random.randint(1,6) + random.randint(1,6))
    
    return n_throws


def print_histo(xs:list) -> None:
    one_percent_count = len(xs) / 100
    count_list = collections.Counter(xs)

    for dice_roll in range(2,13):
        dice_roll_count = count_list[dice_roll]
        if dice_roll_count == 0:
            print(f"{dice_roll}")
            continue
        star_count = int(count_list[dice_roll] // one_percent_count)
        stars = star_count * "*"
        print('{:2} {}'.format(dice_roll,stars))# % f"{dice_roll} {stars}")
