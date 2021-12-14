def only_first_is_odd(input):
    x = input[0]
    if x % 2 == 0:
        return False
    for e in input[1:]:
        if e % 2 == 1:
            break
    return True


print(only_first_is_odd([4,3,2,5,7]))
print(only_first_is_odd([9,3,2,5,7]))

