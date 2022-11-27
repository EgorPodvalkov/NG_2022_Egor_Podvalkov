from flask import Flask, render_template, redirect, request
from datetime import datetime
from news import getNews, addArticle

app = Flask("News")

@app.route('/')
def reader():
    news = getNews()
    return render_template("task3/read.html", data = news)


@app.route('/editor')
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
    return redirect('/editor')

    
app.run(debug=True, host="0.0.0.0", port=8081)
