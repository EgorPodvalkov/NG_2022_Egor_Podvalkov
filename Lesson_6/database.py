import sqlite3
from datetime import datetime
from someUsefullFunctions import saveHtmlString, info, err

# Some common function for db

def prepareDataBaseForChat(nameDB):
    '''Prepares database for chatting'''
    connection = initConnection(nameDB)
    initTableChat(connection)
    connection.close()

def prepareDataBaseForSysInfo(nameDB):
    '''Prepares database for system info'''
    connection = initConnection(nameDB)
    initTableSysInfo(connection)
    connection.close()


def initConnection(path):
    '''Tries to init connection by the path'''
    connection = None
    try:
        connection = sqlite3.connect(path)
        info("Connection established!")
    except sqlite3.Error as e:
        err(e)
        info("Connection failed!")
    return connection


def initTableChat(connection):
    '''Tries to create new table for chat'''
    sql = "CREATE TABLE IF NOT EXISTS messages( id INTEGER PRIMARY KEY, time TEXT NOT NULL, name TEXT NOT NULL, text TEXT NOT NULL)"
    connection.execute(sql)

def initTableSysInfo(connection):
    '''Tries to create new table for system info'''
    sql = "CREATE TABLE IF NOT EXISTS sys_Info( id INTEGER PRIMARY KEY, time TEXT NOT NULL, info TEXT NOT NULL)"
    connection.execute(sql)

# Some special functions for Chat

def addMessageToDB(nameDB, name: str, text: str):
    '''Adds message to db'''
    connection = initConnection(nameDB)
    time = datetime.now().strftime("%d.%m %H:%M")
    name = saveHtmlString(name)
    text = saveHtmlString(text)
    sql = f"INSERT INTO messages(`time`, `name`, `text`) VALUES('{time}', '{name}', '{text}')"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def getMessagesFromDB(nameDB):
    '''Extract rows from databasa'''
    connection = initConnection(nameDB)
    sql = "SELECT * FROM messages;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    return rows

def getMessagesInHtmlTags(nameDB):
    '''Returns nice html vision messages'''
    rows = getMessagesFromDB(nameDB)
    result = ""
    for row in rows:
        result += "<hr>"
        mesId, time, name, text = row
        result += f"<name>{name}</name> <date>{time}</date>"
        result += f"<br><text>{text}</text>"
    # <hr>
    # <name>Egor</name>
    # <date>13.12 20:31</date><br>
    # <text>here will be first message</text>
    return result

# Some special functions for SysInfo

def addSysInfoToDB(nameDB, info: str):
    '''Adds selected by user sysInfo to db'''
    if info != "":
        time = datetime.now().strftime("%d.%m %H:%M")
        connection = initConnection(nameDB)
        sql = f'INSERT INTO sys_Info(`time`, `info`) VALUES("{time}", "{info}")'
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()
    

