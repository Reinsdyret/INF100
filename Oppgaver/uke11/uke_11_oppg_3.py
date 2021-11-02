"""With the cards [2,3,4,5,6,7,8,9,10,11] create a function card_combinations(k, n)
that returns a list of sorted tuples of k cards with a total value of n"""
import itertools

def card_combinations(k,n):
    cards = [2,3,4,5,6,7,8,9,10,11]
    combinations_list = []

    for combination in itertools.combinations(cards,k):
        if sum(list(combination)) == n:
            combinations_list.append(combination)

    return combinations_list
