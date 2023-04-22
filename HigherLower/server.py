from flask import Flask
import random as rd

app = Flask(__name__)

number = rd.randint(0, 9)

@app.route('/')
def welcome():
    return '<h1>Guess a number from 0 to 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'

@app.route('/<int:guess>')
def guess(guess):
    if(guess > number):
        return '<h1>So high</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    elif(guess < number):
        return '<h1>So low</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    else:
        return '<h1>Right</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
