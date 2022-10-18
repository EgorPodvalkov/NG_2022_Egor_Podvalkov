from datetime import datetime
import time
print ("--------------------------------------")

seconds = int(input("Enter count of seconds: "))
days = seconds//(60*60*24)

print("It`s ",days,":",datetime.utcfromtimestamp(seconds).strftime('%H:%M:%S'),sep="")
print("Format - days:hours:minutes:seconds")

print ("--------------------------------------")