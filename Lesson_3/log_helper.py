def separator():
    print("fffffffffffffffffffffffffffffffffffffffffffff")

def log(type, message):
    print(str(type) + ": " + str(message))
 
def err(message):
    log("ERROR",message)

def warn(message):
    log("WARNING",message)

def info(message):
    log("INFO",message)
