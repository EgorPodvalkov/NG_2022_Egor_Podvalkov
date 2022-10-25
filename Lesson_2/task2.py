print("***********************************************")

myStr=input("Enter your list (use ', '): ")
st=set(myStr.split(", "))

print("Your list with unicue values is: ")
for item in st:
    print(item)

print("***********************************************")
