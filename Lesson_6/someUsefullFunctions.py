from datetime import datetime

def saveHtmlString(string: str) -> str:
    '''Returns safe string in html'''
    dct = {
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;',
        '"': '&quot;',
        '`': '&#x60;'
    }
    return ''.join([dct[symbol] 
        if symbol in dct.keys() else symbol 
            for symbol in string.strip()])


def log(type, message):
    time = datetime.now().strftime("%H:%M:%S")
    print(time + " " + str(type) + ": " + str(message))
 
def err(message):
    '''Prints error message'''
    log("ERROR", message)

def warn(message):
    '''Prints warning message'''
    log("WARNING", message)

def info(message):
    '''Prints info message'''
    log("INFO", message)

