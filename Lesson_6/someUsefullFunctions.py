from datetime import datetime
import platform as plt
import psutil

# HTML vision functions

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

def prettyHtmlString(string: str) -> str:
    '''Returns pretty string in html'''
    string = string.strip().replace("\n\n", "<hr class='hr_info'>")
    string = string.replace("\t", '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
    string = string.replace("\n", '<br>')

    return string

# loging functions

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

# system info functions

def getSelectedInfo(keys: list) -> str:
    '''Returns selected info'''
    dct = {
        "Architecture": architectureInfo,
        "Machine": typeMachineInfo,
        "Network": networkNameInfo,
        "Platform": platformInfo,
        "Processor": processorInfo,
        "Python": pythonInfo,
        "Boot_time": bootTimeInfo,
        "CPU": cpuInfo,
        "Memory": memInfo,
        "Disk": diskInfo,
    }
    result = ""
    for key in keys:
        result += dct[key]()
    return result


def architectureInfo():
    return "Architecture: "+str(plt.architecture())+"\n\n"

def typeMachineInfo():
    return "Type of your machine: "+str(plt.machine())+"\n\n"

def networkNameInfo():
    return "Your network name: "+str(plt.node())+"\n\n"

def platformInfo():
    return "Your platform: "+str(plt.platform())+"\n\n"

def processorInfo():
    return "Your processor: "+str(plt.processor())+"\n\n"

def pythonInfo():
    temp="Your python info: \n"
    temp+="\tCompiler: "+str(plt.python_compiler())+"\n"
    temp+="\tImplementation: "+str(plt.python_implementation())+"\n"
    temp+="\tVersion: "+str(plt.python_version())+"\n\n"
    return temp

def bootTimeInfo():
    return "Boot time: "+str(psutil.boot_time())+"\n\n"

def cpuInfo():
    temp="Your CPU info: \n"
    temp+="\t"+str(psutil.cpu_times())+"\n"
    temp+="\t"+str(psutil.cpu_percent())+"\n"
    temp+="\t"+str(psutil.cpu_count())+"\n"
    temp+="\t"+str(psutil.cpu_stats())+"\n"
    temp+="\t"+str(psutil.cpu_freq())+"\n\n"
    return temp

def memInfo():
    temp="Your memory info: \n"
    temp+="\t"+str(psutil.virtual_memory())+"\n"
    temp+="\t"+str(psutil.swap_memory())+"\n\n"
    return temp    

def diskInfo():
    temp="Your disk info: \n"
    temp+="\t"+str(psutil.disk_partitions())+"\n"
    temp+="\t"+str(psutil.disk_usage('/'))+"\n"
    temp+="\t"+str(psutil.disk_io_counters())+"\n\n"
    return temp  