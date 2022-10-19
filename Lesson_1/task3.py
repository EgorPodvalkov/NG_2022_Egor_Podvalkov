print ("--------------------------------------")

seconds = int(input("Enter count of seconds: "))

minutes = seconds // 60
hours = minutes // 60
days = hours // 24

seconds = seconds % 60
minutes = minutes % 60
hours = hours % 24

print("It`s ",days,":",hours,":",minutes,":",seconds,sep="")
print("Format - days:hours:minutes:seconds")

print ("--------------------------------------")