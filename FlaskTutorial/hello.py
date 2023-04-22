from flask import Flask, render_template
app = Flask(__name__)

def make_bold(func):
    def wrapper_func():
        return f'<b>{func()}</b>'
    return wrapper_func

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/student/<name>/<int:age>')
@make_bold
def student(name, age):
    return f'Hi guys, my name\'s {name}, {age} years old'


if __name__ == '__main__':
    app.run(debug='on')
