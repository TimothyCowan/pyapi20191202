#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/basic')
def basic():
    return render_template("hellobasic.html")


@app.route("/adv/", defaults={"name": "defaultuser (nothing passed for name)"})
@app.route("/adv/<name>")
def adv(name):
    return render_template("helloadv.html", joevar=name)


if __name__ == "__main__":
    app.run(port=5052)
