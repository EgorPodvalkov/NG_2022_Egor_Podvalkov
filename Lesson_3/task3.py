from log_helper import *

def askString():
    return input("Enter string: ")

def oneStepElemCounter(string, dict, index):
    if string[index] not in dict.keys():
        dict[string[index]]=1
    else:
        dict[string[index]]+=1
    index+=1
    if(index==len(string)):
        return dict
    else:
        return oneStepElemCounter(string,dict,index)

def elemCounter(string):
    return oneStepElemCounter(string,{},0)


def main():
    separator()
    dct=elemCounter(askString())
    info("Your dictionary with your symbols: " + str(dct))

    separator()

main()