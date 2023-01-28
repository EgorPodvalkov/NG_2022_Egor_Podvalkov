'''
Thread manager for downloading and removed images in lesson 7\n
Main function is mainThread
'''
# other libs
from threading import Thread
from rich.console import Console
# my libs
from myParser import getImageListByUrl
from fileManager import makeFolder, download, removeFolder, addFolderToZip

log = Console().log


# main finction
def mainThread(url: str, folder_name: str):
    """Makes new thread for downloading images into new maked folder, adding this folder to archive and removing it"""
    thread = Thread(target = taskForMainThread, args=(url, folder_name, ))

    thread.start()

    thread.join()



# helpful function
def taskForMainThread(url: str, folder_name: str):
    '''Downloads images into maked folder, adds this folder to archive and removes it'''
    
    images = getImageListByUrl(url)

    downloadWithThreads(images, folder_name)

    addFolderToZip(folder_name)

    removeFolder(folder_name)


def downloadWithThreads(images: list[str], folder_name):
    '''Manages threads for downloading list of images'''
    threads = []
    makeFolder(folder_name)
    
    for image in images:
        threads.append(Thread(target = download, args=(image, folder_name, )))

    log("Number of threads for downloading: " + str(len(threads)))
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
