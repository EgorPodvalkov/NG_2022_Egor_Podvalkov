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
    a=askNumber()
    operation=askOperation()
    b=askNumber()
    return a, operation, b

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def divide(a,b):
    try:    
        return a / b
    except ZeroDivisionError as e:
        err(e)
        return "Infitity"

def pow(a,b):
    return a**b

def root(a,b): 
    try:
        return a**(1/b)
    except ZeroDivisionError as e:
        err(e)
        return "Infitity"

def calculate(a, operation, b):
    match operation:
        case '+': 
            info(f"{a} + {b} = "+str(add(a, b)))
        case '-': 
            info(f"{a} - {b} = "+str(sub(a, b)))
        case '*': 
            info(f"{a} * {b} = "+str(mult(a, b)))
        case '/': 
            info(f"{a} / {b} = "+str(divide(a, b)))
        case 'pow':
            info(f"{a} ^ {b} = "+str(pow(a, b)))
        case 'root': 
            info(f"{a} root {b} = "+str(root(a, b)))
        case _: err(str(operation) + " - is not an operation")



def main():
    separator()

    a, operation, b=getInput()
    calculate(a, operation, b)

    separator()

main()