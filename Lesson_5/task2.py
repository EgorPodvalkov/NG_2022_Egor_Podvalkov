from calculator import calculator
from flask import Flask, render_template, request, redirect

app = Flask("Calculator")

@app.route('/')
def index():
    try:
        temp = open("calculation.txt", "r")
        result = calculator(temp.readline())
        temp.close()
    except:
        result = "None"
    return render_template("task2.html", contents=result)

@app.route('/process')
def getCalulationString():
    temp = open("calculation.txt", "w")
    temp.write(request.args.get('data'))
    temp.close()
    return redirect('/')

app.run(debug=True, host="0.0.0.0", port=8081)