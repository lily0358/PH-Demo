from flask import Flask, render_template, request
from alphabet_turtle import *

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/generic', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        user_input: str = request.form['user_input']
        image: Turtle = turtle_maker(user_input)


        return render_template("generic.html", image = image)


if __name__ == '__main__':
    app.run(debug=True)