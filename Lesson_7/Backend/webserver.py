# other libs
from rich.console import Console
from flask import Flask, request, make_response, send_file
# my libs
from fileManager import path
from theadsManager import mainThread

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
    folder_name = request.args.get('folderName')

    mainThread(url, folder_name)

    return generateResponse("")


@app.route("/download")
def downloadZip():
    '''Send zip file for downloading from website'''
    archive_name = request.args.get('folderName') + ".zip"
    try:
        return send_file(path + archive_name, download_name = "Images.zip")
    except:
        log("Something wrong with sending")


app.run(host="0.0.0.0", port=8081)
