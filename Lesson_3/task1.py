from log_helper import *

def askNumber():
    try:
        return float(input("Enter number: "))
    except ValueError as e:
        err(e)
        return 0

def askOperation():
    return input("Enter operation(+, -, *, /, pow, root):")

def getInput():
    num1=askNumber()
    operation=askOperation()
    num2=askNumber()
    return num1, operation, num2

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def divide(num1,num2):
    try:    
        return num1 / num2
    except ZeroDivisionError as e:
        err(e)
        return "Infitity"

def pow(num1,num2):
    return num1**num2

def root(num1,num2): 
    try:
        return num1**(1/num2)
    except ZeroDivisionError as e:
        err(e)
        return "Infitity"

def calculate(num1, operation, num2):
    match operation:
        case '+': 
            info(f"{num1} + {num2} = "+str(add(num1, num2)))
        case '-': 
            info(f"{num1} - {num2} = "+str(sub(num1, num2)))
        case '*': 
            info(f"{num1} * {num2} = "+str(mult(num1, num2)))
        case '/': 
            info(f"{num1} / {num2} = "+str(divide(num1, num2)))
        case 'pow':
            info(f"{num1} ^ {num2} = "+str(pow(num1, num2)))
        case 'root': 
            info(f"{num1} root {num2} = "+str(root(num1, num2)))
        case _: err(str(operation) + " - is not an operation")



def main():
    separator()

    num1, operation, num2=getInput()
    calculate(num1, operation, num2)

    separator()

main()