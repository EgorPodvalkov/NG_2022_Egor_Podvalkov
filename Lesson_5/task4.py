from flask import Flask, render_template, redirect, request
from datetime import datetime
from news import getNews, addArticle

app = Flask("News")
correct_password = "admin"

@app.route('/')
def reader():
    news = getNews()
    return render_template("task3/read.html", data = news)


@app.route('/editor')
def editorWithoutPass():
    return redirect('/password')


@app.route('/password')
def password():
    return render_template("task4/password.html")


@app.route('/password_checker')
def passwordChecker():
    if correct_password == request.args.get("password"):
        return redirect(f'/editor{correct_password}')
    else:
        return render_template("task4/password.html", error="Incorrect password")
        

@app.route(f'/editor{correct_password}')
def editor():
    return render_template("task3/edit.html")


@app.route('/addNews')
def addNews():

    #getting title
    title = request.args.get('title')

    #getting text
    text = request.args.get('text')

    #getting date
    date = datetime.now().strftime("%d.%m %H:%M")

    addArticle(title, text, date)
    return redirect(f'/editor{correct_password}')

    
app.run(debug=True, host="0.0.0.0", port=8081)
