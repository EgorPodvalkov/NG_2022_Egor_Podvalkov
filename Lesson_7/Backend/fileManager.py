'''
File manager for images in backend for lesson 7\n
Main functions are download, remove, addToZip and clearZip\n
Also you can get images_path and zip_path
'''
from rich.console import Console
from urllib.request import urlretrieve
import os
from zipfile import ZipFile

log = Console().log
images_path = os.getcwd() + "\\images\\"
zip_path = os.getcwd() + "\\images.zip"


# main functions
def download(url: str):
    """Downloads file from url in images folder"""
    try:
        file_name = url.split("/")[-1]
        urlretrieve(url, images_path + file_name)
        log("Image downloaded: " + file_name)
        return file_name
    except:
        log("Something wrong, image doesn`t downloaded.")
        log(url, images_path + file_name)
        return False


def remove(file_name: str):
    """Tries to remove file from images folder"""
    file_path = images_path + file_name
    if os.path.isfile(file_path):
        os.remove(file_path)
        log("File removed: " + file_name)
    else:
        log("File for remove not found: " + file_name)


def addToZip(file_name: str):
    """Adds file to zipfile in path: ...\\Lesson_7\\Backend\\images.zip from images folder"""
    file_path = images_path + file_name
    # checking for file existence
    if os.path.isfile(file_path):
        # adding to zip
        with ZipFile(zip_path, "a") as myzip:
            myzip.write(file_path, arcname = file_name)
        log("File " + file_name + " added to images.zip")
    else:
        log("File for zip not found: " + file_name)


def clearZip():
    '''Removes zipfile in path: ...\\Lesson_7\\Backend\\images.zip''' 
    if os.path.isfile(zip_path):
        os.remove(zip_path)
        log("Zipfile images.zip removed")
    else:
        log("Zipfile images.zip not found")
