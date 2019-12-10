#!/usr/bin/python3

from flask import Flask, session, render_template, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = "random string"

@app.route('/')
def index():
    if "username" in session:
        username = session["username"]
        return "logged in as " + username + "<br>" + "<b><a href = '/logout'>click here to logout"
    return "you are not logged in <br><a href = '/login'>/click here to logout"


if __name__ == '__main__':
    app.run(port=5500)
