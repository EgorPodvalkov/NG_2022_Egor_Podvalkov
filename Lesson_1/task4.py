print ("--------------------------------------")

print("Format ax^2+bx+c=0")
#a=int(input("Enter a: "))
#b=int(input("Enter b: "))
#c=int(input("Enter c: "))
a=1
b=0
c=0
disk=b**2-4*a*c
if disk == 0:
    x=-b/(2*a)
    print("x=",x,sep="")
elif disk>0:
    x1=(disk**0.5-b)/(2*a)
    x2=(-disk**0.5-b)/(2*a)
    print("x1=",x1,sep="")
    print("x2=",x2,sep="")
else :
    print("There is no solution")




print ("--------------------------------------")
