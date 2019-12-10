#!/usr/bin/env python3
from flask import Flask, make_response, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/login')
@app.route("/")
def index():
    return render_template("login.html")


@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "defaultuser"

        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        return resp
    if request.method == "GET":
        return redirect(url_for("index"))


@app.route(("getcookies"))
def getcookie():
    name = request.cookies.get("userID")


if __name__ == "__main__":
    app.run(port=5432)
