"""Make a function dot_product(a,b) that takes in two lists and returns their dot product
Example: a = [1,2,3] b = [3,2,1] dot_product(a,b) = (1*3) + (2*2) + (1*3) = 10"""

def dot_product(a:list,b:list) -> int:
    """Takes in two lists and returns their dot product
    raises ValueError if lists are not equal length"""
    product = 0
    if len(a) != len(b):
        raise ValueError

    zipped_a_b = zip(a,b)

    for x, y in zipped_a_b:
        product += x*y

    return product
