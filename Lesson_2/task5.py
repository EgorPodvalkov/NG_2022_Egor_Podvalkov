print("***********************************************")

myStr=(input("Enter your list (use ','): "))
lst=list(map(int,myStr.split(",")))

max=max(lst)
min=min(lst)
sum=0

for item in lst:
    if item!=max and item!=min:
        sum+=item

print(f"Max is {max}")        
print(f"Min is {min}")        
print(f"Sum is {sum}")        


print("***********************************************")
