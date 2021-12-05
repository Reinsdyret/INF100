"""https://open.kattis.com/problems/numberfun"""

def test_subtraction(num1, num2,result):
    return num1 - num2 == result or num2 - num1 == result

def test_addition(num1, num2,result):
    return num1 + num2 == result

def test_multiplication(num1, num2,result):
    return num1 * num2 == result

def test_division(num1, num2,result):
    return num1 / num2 == result or num2 / num1 == result

n = int(input())

for i in range(n):
    number1, number2, number3 = map(int,input().split(" "))
    if test_subtraction(number1,number2,number3) or test_addition(number1,number2,number3) or test_multiplication(number1,number2,number3) or test_division(number1,number2,number3):
        print("Possible")
    else:
        print("Impossible")
