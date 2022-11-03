from log_helper import *

def getCardNumber():
    return input("Enter card number: ")

def cardChecker(card):
    amexIdentificator=["34", "37"]
    masterIdentificator=["51", "52", "53", "54", "55"]
    visaIdentificator=["4"]
    if card[0:2] in amexIdentificator and len(card)==15:
        result="AMEX"
    elif card[0:2] in masterIdentificator and len(card) == 16:
        result="MASTERCARD"
    elif card[0] in visaIdentificator and (len(card) == 16 or len(card)==13):
        result="VISA"
    else:
        return "INVALID"
    
    try:
        cardLst=list(map(int,card))
    except:
        return "INVALID"

    index=0
    sum=0
    if len(cardLst)%2==1:
        sum+=cardLst[index]
        index+=1
    while index<len(cardLst):
        sum+=2*cardLst[index]
        if 2*cardLst[index]>9:
            sum-=9
        sum+=cardLst[index+1]
        index+=2
    if sum%10==0:
        return result
    else:
        return "INVALID"        

def main():
    separator()
    info(cardChecker(getCardNumber()))

    separator()

main()