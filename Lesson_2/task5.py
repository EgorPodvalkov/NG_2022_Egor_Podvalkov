from asyncio.windows_events import INFINITE
from cmath import inf


print("***********************************************")

myStr=(input("Enter your list (use ', '): "))
lst=myStr.split(", ")

max=int(lst[0])
min=int(lst[0])
sum=-2*int(lst[0])

for item in lst:
    item=int(item)
    if item>=max:
        sum+=max
        max=item
    elif item<=min:
        sum+=min
        min=item
    else:
        sum+=item

print(f"Max is {max}")        
print(f"Min is {min}")        
print(f"Sum is {sum}")        


print("***********************************************")
