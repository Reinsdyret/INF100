"""How many letters are there if you take all numbers from 1-1000 inclusive
and write them out in words. Project Euler problem 17: https://projecteuler.net/problem=17"""
numbers = {
    "" : "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
def number_name(number:int) -> str:
    """Takes in integer and returns the name for that number"""
    number_total_string = ""
    if number <= 20:
        #If the number already is in the numbers dictionary
        number_total_string = numbers[number]
    elif number < 100:
        # If the number consists of two integers
        number_string = str(number)
        if number_string[1] == "0":
            #In case the two integer number is divisible by 10
            number_total_string = numbers[number]
        else:
            # Normal output for two digit number
            number_tens = int(number_string[0] + "0")
            number_ones = int(number_string[1])
            number_total_string = numbers[number_tens] + numbers[number_ones]
    elif number < 1000:
        number_string = str(number)
        if number_string[1] == "0" and number_string[2] == "0":
            # If number is divisible by 100
            number_total_string = numbers[int(number_string[0])] + "hundred"
        elif number_string[1] == "0":
            #If number has no digit in the middle
            number_hundreds = int(number_string[0])
            number_ones = int(number_string[2])
            number_total_string = numbers[number_hundreds] + "hundred" + "and" + numbers[number_ones]
        elif number_string[2] == "0":
            # If number is divisible by 10
            number_hundreds = int(number_string[0])
            number_tens = int(number_string[1] + "0")
            number_total_string = numbers[number_hundreds] + "hundred" + "and" + numbers[number_tens]
        else:
            # Normal 3 digit number
            number_hundreds = int(number_string[0])
            number_tens = int(number_string[1] + "0")
            number_ones = int(number_string[2])
            if (int(number_string[1:]) > 10) and (int(number_string[1:]) < 20):
                number_tens = int(number_string[1:])
                number_ones = ""
            number_total_string = numbers[number_hundreds] + " hundred " + " and " + numbers[number_tens] + numbers[number_ones]
    else:
        return "onethousand"

    return number_total_string
def all_numbernames(N:int) -> int:
    """Takes in N and returns the length of the string to be used for writing out all the numbers"""
    all_numbers_string = ""

    for n in range(1,N + 1):
        all_numbers_string += number_name(n)
    return len(all_numbers_string)
def solve_euler_17():
    """Solve poop"""
    return all_numbernames(1000)