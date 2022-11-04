print("***********************************************")

myStr="aabcDafFeEeeca/..A,,"
# myStr=input("Enter your string: ")

dct={}
for elem in myStr:
    if elem.upper()>"Z" or elem.upper()<"A" or elem in dct.keys():
        continue
    dct[elem]=myStr.count(elem)

print("The list of your letters:")
for key in dct.keys():
    print(f"{key}: {dct[key]}")

sortedKeysByAlph=sorted(dct.keys())
print("The list of your letters sorted by alphabet:")
for key in sortedKeysByAlph:
    print(f"{key}: {dct[key]}")

sortedKeysByNum=sorted(dct, key=dct.get, reverse=True)
print("The list of your letters sorted by numbers:")
for key in sortedKeysByNum:
    print(f"{key}: {dct[key]}")


print("***********************************************")
