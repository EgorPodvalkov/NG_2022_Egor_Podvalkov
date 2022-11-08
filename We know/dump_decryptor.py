from log_helper import *

def inputCipher():
    return input("Enter cipher:\n")

def inputStep():
    try:
        return int(input("\nEnter decrypt what you need: "))
    except:
        return 0

def showAllDecrypts(cipher, maxLen=40):
    for step in range(1,26):            # all possible steps 
        decrypt(cipher, step, maxLen)

def decrypt(cipher, step, maxLen=float("inf")):
    print()
    if step<=0 or step>=26:
        info("Your cipher is: "+ cipher)
        return
    decryptedStr=str(step)+". "
    for index in range(len(cipher)):     # brute force of string
        if cipher[index].upper()>"Z" or cipher[index].upper()<"A":      # if symbol is not a letter
            if index > maxLen:          # if cipher too long we show short version
                decryptedStr+="..."
                break
            decryptedStr+=cipher[index]
            continue
        if ord(cipher[index].upper())+step>ord("Z"):            # decrypt rules
            decryptedStr+=chr(ord(cipher[index])+step-26)
        else:                                                   # decrypt rules
            decryptedStr+=chr(ord(cipher[index])+step)
    info(decryptedStr)       

def main():
    cipher=inputCipher()
    showAllDecrypts(cipher)
    decrypt(cipher, inputStep())

main()