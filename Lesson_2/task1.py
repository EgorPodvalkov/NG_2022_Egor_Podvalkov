print("***********************************************")
again=True
myStr=input("Enter your string: ")

while(again):
    dct={}
    for elem in myStr:
        elem=elem.upper()
        if elem>"Z" or elem<"A":
            continue
        if(elem in dct.keys()):
            dct[elem]=dct[elem]+1
        else:
            dct[elem]=1

    print("Enter 1 to display the number of letter you want,")
    print("enter 2 to display the number of each letter,")
    print("enter 3 to sort and display the number of each letter,")
    print("enter 4 to rewrite your string and")
    print("enter 5 to exit from program.")
    option=input("Your choice is: ")
    match option:
        # one letter
        case "1":
            letter=input("Enter your letter: ")
            if letter.upper() in dct.keys():
                print(f"Your letter '{letter}' was in your string {dct[letter.upper()]} times.")
            else:
                print("There is no this letter in your string(")
        # each letter
        case "2":
            print("The list of your letters:")
            for key in dct.keys():
                print(f"{key}: {dct[key]}")
        # each letter with sorting
        case "3":
            sort=input("Enter 1 to sort by alphabet or 2 to sort by number: ")
            match sort: 
                # sort by alphabet
                case "1":
                    sortedKeys=sorted(dct.keys())
                # sort by number
                case "2":
                    sortedKeys=sorted(dct, key=dct.get, reverse=True)
                # sort by alphabet
                case _:
                    print("Incorect value, let it be sorting by alphabet :)")
                    sortedKeys=sorted(dct.keys())
            print("The sorted list of your letters:")
            for key in sortedKeys:
                print(f"{key}: {dct[key]}")
        # new string
        case "4":
            myStr=input("Enter your new string: ")
        case "5":
            again=False
        case _:
            print("Wrong value, let it be 5, bye!")
            again=False
    print("***********************************************")
