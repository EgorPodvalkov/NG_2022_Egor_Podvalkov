'''
Thread manager for downloading and removed images in lesson 7\n
Main functions are downloadWithThreads and removeWithThreads\n
Also you can use imgNames
'''
# other libs
from threading import Thread
from rich.console import Console
# my libs
from fileManager import download, remove

log = Console().log
imgNames = []


# main finctions
def downloadWithThreads(images: list[str]):
    '''Manages threads for downloading list of images'''
    threads = []

    for image in images:
        threads.append(Thread(target = taskForDownloadingInThread, args=(image, )))

    log("Number of threads for downloading: " + str(len(threads)))
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def removeWithThreads(imageNames: list[str]):
    '''Manages threads for downloading list of images'''
    threads = []

    for image in imageNames:
        threads.append(Thread(target = remove, args=(image, )))

    log("Number of threads for removing: " + str(len(threads)))
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

# helpful function
def taskForDownloadingInThread(image):
    '''Downloads, adds to zip and removes image'''
    imgName = download(image)
    if imgName:
        imgNames.append(imgName)