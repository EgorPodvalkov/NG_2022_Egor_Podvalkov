from log_helper import*

def askString():
    return input("Enter your string: ")

def askOperation():
    print("")
    print("Enter 1 to sort and display your string,")
    print("enter 2 to display the number of each symbol,")
    print("enter 3 to display only vowels or consonants letters,")#vovels(a, o, e, etc.), consonants - other
    print("enter 4 to split by words and to display words in reverse order,")
    print("enter 5 to display word by your number,")
    print("enter 6 to rewrite your string and")
    print("enter 7 to exit from program.")
    try:    
        operation=int(input("Your choice is: "))
        if operation>7 or operation<1:
            raise ValueError(str(operation) + " - no such operation")
        else:
            return operation
    except ValueError as e:
        err(e)
        return askOperation()

def listToString(list):
    string="\""
    for item in list:
        string+=str(item)
    string+="\""
    return string

def sortAndDisplay(string):
    sortedString = sorted(string)
    info(f"Your sorted string is: " + listToString(sortedString))

def numberOfEachSymbol(string):
    dct={}
    for elem in string:
        if elem not in dct.keys():
            dct[elem]=string.count(elem)
    info("The list of your symbols: "+str(dct))

def vowelsOrConsonants(string):
    try:
        vowels=int(input("Enter 1 for vowels, 0 for consonants: "))
        if vowels is 1:
            vowels=True
        elif vowels is 0:
            vowels=False
        else:
            raise ValueError(str(vowels) + " - no such operation")
    except ValueError as e:
        err(e)
        vowelsOrConsonants(string)
    else:
        vowelLetters=["a","e","o","y","u","i"]
        tempString=""
        for item in string:
            if vowels and item.lower() in vowelLetters:
                tempString+=item
            elif not vowels and item.lower() not in vowelLetters and item.lower() !=item.upper():
                tempString+=item
        info("Your string is: "+ tempString)

def splitAndReverse(string):
    words=string.split(" ")
    tempWords=words.copy()
    for index in range(len(words)):
        words[index]=tempWords[-index-1]
    info("Your split and revesed string: "+str(words))

def onlyLettersAndSpaces(string):
    tempString=""
    for item in string:
        if item.lower()!=item.upper() or item==" ":
            tempString+=item
    return tempString

def wordByNumber(string):
    try:
        num=int(input("Enter number of word: "))
    except ValueError as e:
        err(e)
        wordByNumber(string)
    else:
        string=onlyLettersAndSpaces(string)  
        words=string.split(" ")
        try:
            words[num-1]
        except IndexError as e:
            err(e)
            wordByNumber(string)
        else:
            info("Your "+str(num)+" word is "+str(words[num-1]))
            

def main():
    separator()
    again=True
    string=askString()
    while again:
        operation=askOperation()
        separator()
        match operation:
            case 1:
                sortAndDisplay(string)
            case 2:
                numberOfEachSymbol(string)
            case 3:
                vowelsOrConsonants(string)
            case 4:
                splitAndReverse(string)
            case 5:
                wordByNumber(string)
            case 6:
                string=askString()
            case 7:
                again=False
                info("Goodbye!")
            case _:
                err("Wrong operator in def main()")

        separator()

main()
