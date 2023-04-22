from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/<name>')
def welcome(name):
    responseGender = requests.get(url = f'https://api.genderize.io/?name={name}')
    responseGender.raise_for_status()
    responseAge = requests.get(url = f'https://api.agify.io/?name={name}')
    responseAge.raise_for_status()

    return render_template('index.html', gender = responseGender.json(), name = name, age = responseAge.json())

@app.route('/blogs')
def get_blogs():
    response = requests.get(url = 'https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    return render_template('blogs.html', blogs = response.json())

if __name__ == '__main__':
    app.run()