"""Write a program that takes in two integers and returns the prodcuct but in a special way"""

def multiplication_table(binNum:str,a:list,b:list) -> str:
    """Take in binary number, list a and b and return a multiplication table as string"""
    string = ""
    binNum = binNum[::-1]
    for i in range(len(a)):
        string += '%-1s%5i%5i' % (binNum[i], a[i], b[i]) + "\n"

    return string[:-1]

def addition_department(binNum:str, a:list, b:list, factorA:int, factorB:int) -> str:
    row1 = ""
    sumRow1 = 0
    row2 = ""
    binNum = binNum[::-1]
    for i in range(len(binNum)):
        if binNum[i] == "X":
            row1 += f"{a[i]} + "
            sumRow1 += a[i]
            row2 += f"{b[i]} + "

    row1 = row1[:-2]
    row2 = row2[:-2]
    string = f"{row1}= {sumRow1}\n{row2}= {factorA*factorB}"
    return string
    
    


factorA = int(input("Factor A: "))
factorB = int(input("Factor B: "))

switched = False

# In case that a is not lower than b
if factorA > factorB:
    temp = factorA
    factorA = factorB
    factorB = temp
    switched = True

binaryA = bin(factorA)
binaryA = binaryA[2:]

binaryListA = []
for i in range(0,len(binaryA)):
    binaryListA.append(2 ** i)

numberListB = []
for i in range(0,len(binaryA)):
    numberListB.append(factorB << i)

xString = ""
for num in binaryA:
    xString += "X" if num == "1" else " "

if switched:
    temp = factorA
    factorA = factorB
    factorB = temp

print("=========================")
print(multiplication_table(xString,binaryListA,numberListB))
print("=========================")
print(addition_department(xString,binaryListA,numberListB,factorA,factorB))
print("=========================")
print(f"{factorA} * {factorB} = {factorB*factorA}")
