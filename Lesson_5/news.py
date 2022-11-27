"""Contains functions to reading news from and adding news to txt file"""

def getNews():
    """Returns string of news with html format from file News.txt"""
    try:
        file = open("News.txt","r")
        news = ""
        for article in file.readlines():
            news += article
        file.close()
        if news == "":
            raise Exception()
    except:
        news = "<h2>No news :(</h2>"
    return news

def addArticle(title, text, date):
    """Adds article with html format to txt file"""

    news = getNews()
    if news == "<h2>No news :(</h2>":
        news = ""

    if title == "":
        title = "No title :("

    if text == "":
        text = "No text :("

    file = open("News.txt", "w")
    file.write(
    f"<h2>{title}</h2>" + 
    f"<h4>{date}</h4>" + 
    f"<h3>{text}</h3>" + 
    "<hr />" + news)
    file.close()