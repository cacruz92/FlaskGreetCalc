from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def greet():
    return "welcome"

@app.route('/welcome/home')
def greet():
    return "welcome home"

@app.route('/welcome/back')
def greet():
    return "welcome back"