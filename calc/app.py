# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add(a,b):
    return a+b

@app.route('/sub')
def sub(a,b):
    return a-b

@app.route('/mult')
def mult(a,b):
    a*b

@app.route('/div')
def div(a,b):
    return a/b