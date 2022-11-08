import platform as plt
import psutil

def architectureInfo(): #a
    return "Architecture: "+str(plt.architecture())+"\n\n"

def typeMachineInfo():  #b
    return "Type of your machine: "+str(plt.machine())+"\n\n"

def networkNameInfo():  #c
    return "Your network name: "+str(plt.node())+"\n\n"

def platformInfo():     #d
    return "Your platform: "+str(plt.platform())+"\n\n"

def processorInfo():    #e
    return "Your processor: "+str(plt.processor())+"\n\n"

def pythonInfo():       #f
    temp="Your python info: \n"
    temp+="\tCompiler: "+str(plt.python_compiler())+"\n"
    temp+="\tImplementation: "+str(plt.python_implementation())+"\n"
    temp+="\tVersion: "+str(plt.python_version())+"\n\n"
    return temp

def bootTimeInfo():     #g
    return "Boot time: "+str(psutil.boot_time())+"\n\n"

def cpuInfo():          #h
    temp="Your CPU info: \n"
    temp+="\t"+str(psutil.cpu_times())+"\n"
    temp+="\t"+str(psutil.cpu_percent())+"\n"
    temp+="\t"+str(psutil.cpu_count())+"\n"
    temp+="\t"+str(psutil.cpu_stats())+"\n"
    temp+="\t"+str(psutil.cpu_freq())+"\n\n"
    return temp

def memInfo():          #i
    temp="Your memory info: \n"
    temp+="\t"+str(psutil.virtual_memory())+"\n"
    temp+="\t"+str(psutil.swap_memory())+"\n\n"
    return temp    

def diskInfo():         #j
    temp="Your disk info: \n"
    temp+="\t"+str(psutil.disk_partitions())+"\n"
    temp+="\t"+str(psutil.disk_usage('/'))+"\n"
    temp+="\t"+str(psutil.disk_io_counters())+"\n\n"
    return temp  

def writeToFileController(dct):
    dataFile = open("info.txt","w")
    if dct["a"][1]:
        dataFile.write(architectureInfo())
    if dct["b"][1]:
        dataFile.write(typeMachineInfo())
    if dct["c"][1]:
        dataFile.write(networkNameInfo())
    if dct["d"][1]:
        dataFile.write(platformInfo())
    if dct["e"][1]:
        dataFile.write(processorInfo())
    if dct["f"][1]:
        dataFile.write(pythonInfo())
    if dct["g"][1]:
        dataFile.write(bootTimeInfo())
    if dct["h"][1]:
        dataFile.write(cpuInfo())
    if dct["i"][1]:
        dataFile.write(memInfo())
    if dct["j"][1]:
        dataFile.write(diskInfo())
    dataFile.close

def menuController(dct):
    for key in dct.keys():      #output menu
        if dct[key][1]:
            indicator = "\t(yes)"
        else:
            indicator = "\t(no)"
        print(key+") "+dct[key][0]+indicator)
    print("y) Proceed")

    string=input("Choose variants what you want to add or to del: ")
    for key in dct.keys():      #analyze input 
        if key in string:
            dct[key][1] = not dct[key][1]

    if "y" in string:           #proceed program
        return dct
    else:
        return menuController(dct)


def main():
    dct = {"a": ["Architecture", False],
        "b": ["Machine type", False],
        "c": ["Network name", False],
        "d": ["Platform", False],
        "e": ["Processor", False],
        "f": ["Python info", False],
        "g": ["Boot time", False],
        "h": ["CPU info", False],
        "i": ["Memory info", False],
        "j": ["Disk info", False]}
    writeToFileController(menuController(dct))

main()
