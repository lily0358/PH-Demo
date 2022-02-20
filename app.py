from flask import Flask, render_template, request
from alphabet_turtle import *

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/second")
def second():
    main()
    return render_template('index.html/second')

if __name__ == '__main__':
    app.run(debug=True)