print("***********************************************")

inputValue=int(input("Enter number: "))

while inputValue>0:
    outputValue=inputValue
    while outputValue>0:
        print(outputValue,end=" ")
        outputValue-=1
    inputValue-=1
    print("")


print("***********************************************")
