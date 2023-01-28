'''
File manager for images in backend for lesson 7\n
Main functions are makeFolder, download, removeFolder and addFolderToZip\n
Also you can get path
'''
from rich.console import Console
from urllib.request import urlretrieve
import os
from zipfile import ZipFile
from shutil import rmtree

log = Console().log
path = os.getcwd() + "\\"


# main functions
def makeFolder(folder_name: str):
    '''Makes folder in path: ...\\Lesson_7\\Backend\\"folder_name"'''
    os.mkdir(path + folder_name)


def download(url: str, folder_name: str):
    """Downloads file from url in folder"""
    try:
        file_name = url.split("/")[-1]
        urlretrieve(url, path + folder_name + "\\" + file_name)
        log("Image downloaded: " + file_name)

    except:
        log("Something wrong, image doesn`t downloaded.")
        log(path + folder_name + "\\" + file_name)


def removeFolder(folder_name: str):
    """Tries to remove file from images folder"""
    try:
        rmtree(path + folder_name)
        log("Folder removed: " + folder_name)
    except:
        log("Folder for remove not found: " + folder_name)


def addFolderToZip(folder_name: str):
    """Adds all files in folder to zipfile in path: ...\\Lesson_7\\Backend\\'folder_name'.zip"""
    folder_path = path + folder_name
    for file_name in os.listdir(folder_path):
        # adding to zip
        try:
            with ZipFile(folder_path + ".zip", "a") as myzip:
                myzip.write(folder_path + "\\" + file_name, arcname = file_name)
            log("File " + file_name + " added to " + folder_name + ".zip")
        except:
            log("File for zip not found: " + file_name)

