# other libs
from rich.console import Console
from flask import Flask, request, make_response, send_file
# my libs
from myParser import getImageListByUrl
from fileManager import addToZip, clearZip, zip_path
from theadsManager import imgNames, downloadWithThreads, removeWithThreads

log = Console().log
app = Flask("ZipperBack")


def generateResponse(data):
    """Returns response with data"""
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/getUrl")
def getUrl():
    """Downloads all pictures from url and packed them to archive"""
    url = request.args.get('url')

    images = getImageListByUrl(url)
    clearZip()
    imgNames.clear()

    downloadWithThreads(images)

    for imgName in imgNames:
        addToZip(imgName)

    removeWithThreads(imgNames)

    return generateResponse("")


@app.route("/images.zip")
def downloadZip():
    '''Send zip file for downloading from website'''
    try:
        return send_file(zip_path, download_name = "Images.zip")
    except:
        log("Something wrong with sending")


app.run(host="0.0.0.0", port=8081)
