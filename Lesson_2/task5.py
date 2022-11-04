print("***********************************************")

myStr=(input("Enter your list (use ','): "))
lst=list(map(int,myStr.split(",")))

max=max(lst)
min=min(lst)
sum=sum(lst)-min-max

print(f"Max is {max}")        
print(f"Min is {min}")        
print(f"Sum is {sum}")        


print("***********************************************")
