print ("--------------------------------------")


print ("Enter a: ", end = "")
a = int(input())
print ("Enter b: ", end = "")
b = int(input())
print ("Enter operation(+, -, *, /, sq(square), root): ", end = "")
operation = input()


match operation:
    case '+':print("a+b=", a+b, sep="")
    case '-': print("a-b=", a-b, sep="")
    case '*': print("a*b=", a*b, sep="")
    case '/': print("a/b=", a/b, sep="")
    case 'sq' | 'square': 
        print("a^2=", a**2, sep="")
        print("b^2=", b**2, sep="")
    case 'root': print("a root b is", a**(1/b))
    case _: print("Error:",operation,"- is not an operation")


print ("--------------------------------------")


