print("***********************************************")

myStr=(input("Enter your list (use ', '): "))
lst=myStr.split(", ")

max=int(lst[0])
min=int(lst[0])
sum=0
for item in lst:
    item=int(item)
    if item>max:
        max=item
    if item<min:
        min=item
for item in lst:
    item=int(item)
    if item!=max and item!=min:
        sum+=item
print(f"Max is {max}")        
print(f"Min is {min}")        
print(f"Sum is {sum}")        


print("***********************************************")
