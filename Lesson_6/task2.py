from flask import Flask, render_template, request, redirect
from database import prepareDataBaseForSysInfo, addSysInfoToDB
from someUsefullFunctions import getSelectedInfo, prettyHtmlString

NAME_DB = "SysInfo.db"

app = Flask("SysInfo")
prepareDataBaseForSysInfo(NAME_DB)

@app.route('/')
def index():

    keys = list(request.args)
    info = getSelectedInfo(keys)
    addSysInfoToDB(NAME_DB, info)
    return render_template("task2.html", checked = keys, info = prettyHtmlString(info))

app.run(host="0.0.0.0", port="8080", debug=True)