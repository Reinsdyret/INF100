""""Use the given function collatz_sequence(n) to make a dictonary of the 10 first collatz sequences
function ten_first_collatz"""


def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def first_ten_collatz():
    """Make a dictonary of the first 10 collatz sequences"""
    ten_collatz = {
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None,
        7:None,
        8:None,
        9:None,
        10:None
    }
    for key in range(1,11):
        ten_collatz[key] = collatz_sequence(key)
    return ten_collatz


print(first_ten_collatz())
