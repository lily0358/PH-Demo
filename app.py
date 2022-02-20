from flask import Flask, render_template, request
from alphabet_turtle import *

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("result.html", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        print("hello world")
        user_input: str = request.form['user_input']
        main()


        return render_template("result.html")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)