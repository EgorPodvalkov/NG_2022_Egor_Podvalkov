"""Contains functions calculator and calculate"""

def calculate(num1, operation, num2):
    """Returns result of calculation"""
    match operation:
        case '+': 
            return f"{num1} + {num2} = "+str(add(num1, num2))
        case '-': 
            return f"{num1} - {num2} = "+str(sub(num1, num2))
        case '*': 
            return f"{num1} * {num2} = "+str(mult(num1, num2))
        case '/': 
            return f"{num1} / {num2} = "+str(divide(num1, num2))
        case 'pow' | '^':
            return f"{num1} ^ {num2} = "+str(pow(num1, num2))
        case 'root': 
            return f"{num1} root {num2} = "+str(root(num1, num2))
        case _: 
            return str(operation) + " - is not an operation"

def calculator(string):
    """Returns result of calculation"""
    operations = ["+","-","*","/",
                "pow", "^", "root"]
    
    #clearing from spaces
    temp_string = ""
    for item in string:
        if item == " ":
            continue
        temp_string += item
    string = temp_string
    if string == "":
        return "None"

    #geting operation index
    index = None
    for item in operations:
        try:
            index = string.index(item)
            operation = item
            break
        except:
            continue
    if index == None:
        return "You forget operation sign!!!"

    #getting num1
    try:                    
        num1 = int(string[:index])
    except:
        return string[:index] + " is NaN"
    index += len(operation)

    #getting num2
    try:
        num2 = int(string[index:])
    except:
        return string[index:] + " is NaN"

    #getting result
    return calculate(num1, operation, num2)


def add(num1,num2):
    """Returns sum"""
    return num1 + num2

def sub(num1,num2):
    """Returns difference"""
    return num1 - num2

def mult(num1,num2):
    """Returns product"""
    return num1 * num2

def divide(num1,num2):
    """Returns fraction"""
    try:    
        return num1 / num2
    except ZeroDivisionError as e:
        return "Infitity"

def pow(num1,num2):
    """Returns pow"""
    return num1**num2

def root(num1,num2): 
    """Returns root"""
    try:
        return num1**(1/num2)
    except ZeroDivisionError as e:
        return "Infitity"
