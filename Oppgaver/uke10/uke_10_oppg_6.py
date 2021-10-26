"""Make function add_together_safely(a,b,c,d) that safely can add 4 parameters"""

def add_together(a, b, c, d):
    return a + b + c + d


def add_together_safely(a,b,c,d):
    try:
        return add_together(a,b,c,d)
    except TypeError as type_error:
        print(f"Failed with error: {type_error}")

print(add_together_safely('a','story','with','cake'))