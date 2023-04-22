from flask import Flask, render_template, request
import requests

app = Flask(__name__)
response = requests.get(url = 'https://api.npoint.io/9bf2f6d7579d4ab89684')
response.raise_for_status()
data = response.json()

@app.route('/')
def home():
    return render_template('index.html', blogs = data)

@app.route('/detail-post/<int:id>')
def detail_post(id):
    post = None
    for blog in data:
        if blog['id'] == id:
            post = blog
            break
    return render_template('post.html', blog = post)

@app.route('/contact', methods = ["POST", "GET"])
def contact():
    if(request.method == 'GET'):
        return render_template('contact.html')
    else:
        return render_template('contact.html', message = 'Successfully sent message')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()